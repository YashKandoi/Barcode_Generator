from flask import Flask, request, jsonify
import requests
import json
import subprocess
import sys
import openai_code as oai

app = Flask(__name__)

@app.route('/process_data', methods=['POST'])
def process_data():
    # Get the file path, tax percentage, and profit percentage from the request
    file_path = request.form.get('file_path')
    tax_percentage = float(request.form.get('tax_percentage'))
    profit_percentage = float(request.form.get('profit_percentage'))

    # Perform the data processing steps
    url = 'https://app.nanonets.com/api/v2/OCR/Model/ef653ad5-a2fd-486e-af23-d9ec6b677db5/LabelFile/?async=false'

    data = {'file': open(file_path, 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('a71e898c-f947-11ed-98af-ce47f9786cdf', ''), files=data)
    response_json = response.json()
    with open('response.json', 'w') as file:
        json.dump(response_json, file)

    delete_fields_from_json('response.json', ['id', 'xmin', 'ymin', 'xmax', 'ymax', 'score', 'verification_status',
                                              'failed_validation', 'label_id', 'status'])

    with open('response.json') as f:
        data = json.load(f)

    with open('response.txt', 'w') as f:
        json.dump(data, f)

    with open('response.txt', 'r') as f:
        data = f.read()

    x = 'Identify seller, products, price, line_amount, and their quantity from this JSON file. ' \
        'Don’t include the courier charge\n' + data
    y = oai.getReply(x)
    a = 'Please use this information and generate a table as per product with their individual prices ' \
        'after adding a ' + str(tax_percentage) + '% tax on the line amount and ' + str(profit_percentage) + '% ' \
                                                                                                            'profit after that. ' \
                                                                                                            'Please output the ' \
                                                                                                            'following fields: ' \
                                                                                                            'seller, product, price, ' \
                                                                                                            'quantity, line_amount, Tax ' \
                                                                                                            '%, Tax, Profit %, Profit, ' \
                                                                                                            'Final Price(After tax and ' \
                                                                                                            'profit), final price per ' \
                                                                                                            'piece and barcode for each ' \
                                                                                                            'product. ' \
                                                                                                            'If the quantity is more ' \
                                                                                                            'than one, display it for ' \
                                                                                                            'each piece. ' \
                                                                                                            'Please round off all ' \
                                                                                                            'figures to the nearest ' \
                                                                                                            'integer. Please generate ' \
                                                                                                            'a sequentially increasing ' \
                                                                                                            '12 digit number as a barcode ' \
                                                                                                            'for each product piece. ' \
                                                                                                            'You should have duplicate ' \
                                                                                                            'entries for products having ' \
                                                                                                            'more than one quantity, so ' \
                                                                                                            'that each individual item ' \
                                                                                                            'of the same product has a ' \
                                                                                                            'different barcode'

    z = oai.getReply(a + "\n" + y)
    d = oai.getReply("Please convert the following information into a .csv file format\n" + z)
    oai.createCSV(d)

    file_path = 'temp.csv'
    open_csv_file(file_path)

    # Return a response
    response = {'message': 'Data processed successfully'}
    return jsonify(response)

def delete_fields_from_json(json_file_path, fields_to_delete):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    for item in data['result']:
        if 'prediction' in item:
            for prediction in item['prediction']:
                for field in fields_to_delete:
                    if field in prediction:
                        del prediction[field]

    for item in data['result']:
        if 'prediction' in item:
            for prediction in item['prediction']:
                if 'cells' in prediction:
                    for cell in prediction['cells']:
                        for field in fields_to_delete:
                            if field in cell:
                                del cell[field]

    for item in data['result']:
        del item['page']
        del item['request_file_id']
        del item['filepath']
        del item['id']
        del item['rotation']
        del item['file_url']
        del item['request_metadata']
        del item['processing_type']

    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)


def open_csv_file(file_path):
    try:
        if sys.platform.startswith('darwin'):  # macOS
            subprocess.run(['open', file_path])
        elif sys.platform.startswith('linux'):  # Linux
            subprocess.run(['xdg-open', file_path])
        elif sys.platform.startswith('win'):  # Windows
            subprocess.run(['start', file_path], shell=True)
        else:
            print("Unsupported operating system.")
    except Exception as e:
        print(f"Error occurred while opening the file: {e}")

if __name__ == '__main__':
    app.run(debug=True)

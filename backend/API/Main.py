import requests
import json
import subprocess
import sys

from .OpenAI_Prompt import *
from .Nanonets_API import *

def delete_fields_from_json(json_file_path, fields_to_delete):
    with open(json_file_path, "r") as file:
        data = json.load(file)

    for item in data["result"]:
        if "prediction" in item:
            for prediction in item["prediction"]:
                for field in fields_to_delete:
                    if field in prediction:
                        del prediction[field]

    for item in data["result"]:
        if "prediction" in item:
            for prediction in item["prediction"]:
                if "cells" in prediction:
                    for cell in prediction["cells"]:
                        for field in fields_to_delete:
                            if field in cell:
                                del cell[field]

    for item in data["result"]:
        del item["page"]
        del item["request_file_id"]
        del item["filepath"]
        del item["id"]
        del item["rotation"]
        del item["file_url"]
        del item["request_metadata"]
        del item["processing_type"]

    with open(json_file_path, "w") as file:
        json.dump(data, file, indent=4)


def open_csv_file(file_path):
    try:
        if sys.platform.startswith("darwin"):  # macOS
            subprocess.run(["open", file_path])
        elif sys.platform.startswith("linux"):  # Linux
            subprocess.run(["xdg-open", file_path])
        elif sys.platform.startswith("win"):  # Windows
            subprocess.run(["start", file_path], shell=True)
        else:
            print("Unsupported operating system.")
    except Exception as e:
        print(f"Error occurred while opening the file: {e}")

def execute_code(file_path, tax_percentage, profit_percentage):
    # url = 'https://app.nanonets.com/api/v2/OCR/Model/ef653ad5-a2fd-486e-af23-d9ec6b677db5/LabelUrls/?async=false'

    # headers = {
    # 'accept': 'application/x-www-form-urlencoded'
    # }

    # data = {'file': open(file_path, 'rb')}

    # response = requests.post(url, auth=requests.auth.HTTPBasicAuth('a71e898c-f947-11ed-98af-ce47f9786cdf', ''), files=data)

    # # url = "https://app.nanonets.com/api/v2/OCR/Model/ef653ad5-a2fd-486e-af23-d9ec6b677db5/LabelFile/?async=false"

    # # data = {"file": open(file_path, "rb")}
    # # response_json = nanonet_call(data)

    # # data = json.loads(response_json)

    # # Extract required information
    # response_json_string = response.json()
    # print(response_json_string)
    url1 = 'https://app.nanonets.com/api/v2/OCR/Model/ef653ad5-a2fd-486e-af23-d9ec6b677db5/LabelFile/?async=false'

    data1 = {'file': open(file_path, 'rb')}

    response1 = requests.post(url1, auth=requests.auth.HTTPBasicAuth('a71e898c-f947-11ed-98af-ce47f9786cdf', ''), files=data1)

    response_json = response1.json()

    # with open("response.json", "w") as file:
    #     json.dump(response_json, file)

    # print(response.text)
    
    result = response_json['result'][0]

    parsed_data = {
        "message": "Success",
        "result": []
    }

    for prediction in result['prediction']:
        label = prediction['label']
        ocr_text = prediction['ocr_text']
        page_no = prediction['page_no']

        parsed_data["result"].append({
            "label": label,
            "ocr_text": ocr_text,
            "type": "field",
            "page_no": page_no
        })

    # Add table data to parsed_data
    table_data = result['prediction'][-1]
    parsed_table_data = {
        "label": table_data['label'],
        "ocr_text": table_data['ocr_text'],
        "type": "table",
        "cells": []
    }

    for cell in table_data['cells']:
        parsed_table_data["cells"].append({
            "row": cell['row'],
            "col": cell['col'],
            "row_span": cell['row_span'],
            "col_span": cell['col_span'],
            "label": cell['label'],
            "text": cell['text'],
            "row_label": cell['row_label']
        })

    parsed_data["result"].append(parsed_table_data)

    # Add size data to parsed_data
    parsed_data['size'] = result['size']

    # Add signed_urls to parsed_data
    parsed_data['signed_urls'] = response_json['signed_urls']

    # Convert parsed_data to JSON format
    data = json.dumps(parsed_data, indent=4)

    x = "Identify seller, products, price, line_amount, and their quantity from this JSON file. Don’t include the courier charge\n" + data
    y = getReply(x)
    a = "Please use this information and generate a table as per product with their individual prices after adding a " + str(tax_percentage) + "% tax on the line amount and " + str(profit_percentage) + "% profit after that. Please output the following fields: seller, product, price, quantity, line_amount, Tax %, Tax, Profit %, Profit, Final Price(After tax and profit), final price per piece and sequentially increasing 12 digit number as a barcode for each product. If the quantity is more than one, display it for each piece. Please round off all monetary values to the nearest two decimal places, and all other figures to the nearest integers. Please generate a sequentially increasing 12 digit number as a barcode for each product piece. You should have duplicate entries for products having more than one quantity, so that each individual item of the same product has a different barcode."
    b = "The output would look something like this: " + open("template.csv","r").read() + "\n please note that the above information should not be included in the output!"
    z = getReply(a + "\n" + b + "\n" + y)
    d = getReply("Please convert the following information into a .csv file format\n" + z)
    createCSV(d)

    file_path = "temp.csv"
    open_csv_file(file_path)
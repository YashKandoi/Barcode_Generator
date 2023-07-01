import requests
import json

url = 'https://app.nanonets.com/api/v2/OCR/Model/ef653ad5-a2fd-486e-af23-d9ec6b677db5/LabelFile/?async=false'

# change filename here as required
data = {'file': open('IMG_6424.jpg', 'rb')}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth('a71e898c-f947-11ed-98af-ce47f9786cdf', ''), files=data)

response_json=response.json()
with open('response.json', 'w') as file:
    json.dump(response_json, file)


def delete_fields_from_json(json_file_path, fields_to_delete):
    # Read the JSON file and parse its contents
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    # Delete the specified fields
    for item in data['result']:
        if 'prediction' in item:
            for prediction in item['prediction']:
                for field in fields_to_delete:
                    if field in prediction:
                        del prediction[field]

    # Delete the specified fields from table
    for item in data['result']:
        if 'prediction' in item:
            for prediction in item['prediction']:
                if 'cells' in prediction:
                    for cell in prediction['cells']:
                        for field in fields_to_delete:
                            if field in cell:
                                del cell[field]
    
    del data['signed_urls']

    # Save the modified JSON to the same file
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Example usage
json_file_path = 'response.json'
fields_to_delete = ['id','xmin', 'ymin', 'xmax', 'ymax', 'score', 'verification_status', 'failed_validation', 'label_id','status']

delete_fields_from_json(json_file_path, fields_to_delete)

print("Response saved to response.json")


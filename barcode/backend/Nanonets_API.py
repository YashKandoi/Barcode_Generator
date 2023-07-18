import requests

def nanonet_call(data):
    url = "https://app.nanonets.com/api/v2/OCR/Model/ef653ad5-a2fd-486e-af23-d9ec6b677db5/LabelFile/?async=false"

    nanonets_api_key = open("nanonets_key.txt","r").read().strip("\n")
    response = requests.post(
        url,
        auth=requests.auth.HTTPBasicAuth(nanonets_api_key, ""),
        files=data,
    )
    response_json = response.json()
    return response_json
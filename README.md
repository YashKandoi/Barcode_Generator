# Track 2 LLM API Endpoint : Barcode_Generator

An AI based barcode generator which enables you to generate barcode of products by uploading their invoice and input the tax and profit percentage.
Check out the demo video here: [https://lnkd.in/dQA2NaJA](https://drive.google.com/file/d/1yePaWPwNxN2HSAFCRaMqfFODaMGJ3_0U/view)
We will soon be deploying this and releasing it for everyone to be able to use!

## How to Use

### Prereqs
Run the following command in terminal:
pip install -r requirements.txt

### Run API
1. Create a secret API key from https://app.nanonets.com/#/keys and paste it in nanonets_key.txt

2. Create a secret API key from https://platform.openai.com/account/api-keys and paste it in openai_key.txt

If the key does not seem to work, then create a new OpenAI account with a different phone number and create a new key from that account

Open a terminal and run the following command: python3 PostmanRunner.py

Let the program run in the background

Open the PostMan application on your computer, insert http://localhost:5000/api/generateBarCode (the link may differ based on your system's local host) in the POST prompt in a new tab on your workspace, and click on "Send"

If for any reason you are unable to use the PostMan application or encounter any errors, you can run the App.py file with this command on your terminal: python3 App.py

Upload files in jpg format only!

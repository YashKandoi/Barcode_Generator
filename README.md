
# AI Arena 1.0: Barcode_Generator

An AI based barcode generator which enables you to generate barcode of products by uploading their invoice and input the tax and profit percentage.
Check out the demo video here: [https://drive.google.com/file/d/1WUWSJj-DN5u7FcSOgGZZxJ4j1EQnYcar/view?usp=sharing]
## How to Use

### Prereqs
Run the following command in terminal:
pip install -r requirements.txt

### Run API
1. Create a secret API key from https://platform.openai.com/account/api-keys and paste it in openai_key.txt
2. Go to openai_key.txt file and paste this there.

If the key does not seem to work, then create a new OpenAI account with a different phone number and create a new key from that account

Open a terminal and run the following command: python3 manage.py runserver

A local host link will be seen on the server. Click on this link to open the page.
Input the file, the tax_percentage and the profit_percentage.

Upload files in jpg format only!

from flask import Flask
import frontend

app = Flask(__name__)

@app.route('/api/generateBarCode', methods=['POST'])
def generateBarCode():
    frontend.upload_file()
    frontend.execute_code()
if __name__ == '__main__':
    app.run()
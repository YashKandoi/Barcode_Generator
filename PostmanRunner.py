from flask import Flask
import Main

app = Flask(__name__)

@app.route('/api/generateBarCode', methods=['POST'])
def generateBarCode():
    Main.main()
    return {}
if __name__ == '__main__':
    app.run()
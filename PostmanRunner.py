from flask import Flask,send_file
import Main

app = Flask(__name__)

@app.route('/api/generateBarCode', methods=['POST'])
def generateBarCode():
    Main.main()
    file_path = "temp.csv"
    return send_file(file_path, mimetype='text/csv', as_attachment=True)
if __name__ == '__main__':
    app.run()
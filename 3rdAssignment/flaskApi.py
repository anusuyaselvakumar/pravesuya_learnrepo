from flask import Flask,jsonify
from data.hi import read,outputEx5

app = Flask(__name__)

@app.route('/api/printHello')
def first():
    return ("Hello World")

@app.route('/api/originalData')
def second():
    data = read()
    return jsonify(data)

@app.route('/api/modifyRecepie')
def modifyOutput():
    data = outputEx5()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
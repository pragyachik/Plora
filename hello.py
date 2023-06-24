from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/returnjson', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
            "text" : "Hello, World!",
        }

        if data:
            with open('data.json', 'w') as json_file:
                json.dump(data, json_file)  # Write the JSON data to the file

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


if __name__ == '__main__':
    app.run()
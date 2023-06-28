from flask import Flask, jsonify, request
import json
import random
# from flask_cors import CORS


app = Flask(__name__)
# CORS(app)

@app.route("/api")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/gettoken", methods = ["POST"])
def get_token():
    data = json.loads(request.data)
    print(data)
    token = random.randint(0,10000)
    with open(str(token)+'.json', 'w') as f:
        f.write(json.dumps(data, indent=2))
    

    response = jsonify({"token":token})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/returnjson', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        value = "Hello, World!"
        try:
            with open('../pickdrop/output.json', 'r') as myfile:
                outputdata=myfile.read()
            #result = client.predict("sound.mp3",api_name="/predict")
            #print(result)
            #transcriptions = model.transcribe(audio_paths)
            #value = transcriptions[0]['transcription']
            #value = result
            value = str(json.loads(outputdata))
        except Exception as e:
            print("The error")
            print(e)
            value = "An Error occurred: "+str(e)

        #data = {
        #    "text" : value,
        #}

        data = value

        #if data:
        #    with open('data.json', 'w') as json_file:
        #        json.dump(data, json_file)  # Write the JSON data to the file

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

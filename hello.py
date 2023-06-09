from flask import Flask, jsonify, request
import json
import random
import datetime
# from flask_cors import CORS
import os


app = Flask(__name__)
# CORS(app)

@app.route("/api")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/getRedPajamaToken", methods = ["POST"])
def get_token():
    data = json.loads(request.data)
    print(data)
    token = random.randint(0,10000)
    created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    token_item = {
            "token":str(token),
            "status":"Not Processed",
            "createdAt":str(created_at)
        }
    
    # Check if the directory exists
    if not os.path.exists('./tokens/'):
        os.makedirs('./tokens/')

    with open('tokens/'+str(token)+'.json', 'w') as f:
        f.write(json.dumps(data, indent=2))
    
    # Define the path to your JSON file
    json_file_path = "./allTokens.json"

    # Check if the JSON file exists
    if not os.path.exists(json_file_path):
        # Create an empty JSON file
        with open(json_file_path, "w") as json_file:
            json.dump([], json_file)

    with open(json_file_path, 'r') as f:
        allTokensData = json.load(f)

    allTokensData.append(token_item)

    with open(json_file_path, 'w') as f:
        f.write(json.dumps(allTokensData, indent=2))
    

    response = jsonify({"token":token})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/getTokenOutput', methods = ['POST'])
def get_token_output():
    data = json.loads(request.data)
    print(data)
    token = data['token']
    responseData = {
        "message": "error"
    }
    token_output_path = './tokenOutputs/'+str(token)+'.json'
    if os.path.exists(token_output_path):
        with open(token_output_path, 'r') as f:
            responseData = json.load(f)
    else:
        responseData = {
            "message": "token not processed"
        }

    response = jsonify(responseData)
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

from flask import Flask,make_response,jsonify,request
from flask_cors import CORS
from controller import usernamecontroller,toxiccontroller
import os
from dotenv import load_dotenv

app=Flask(__name__)
CORS(app)
load_dotenv()
@app.route(os.getenv('py_model_api_link'),methods=['POST'])
def usernickname():
    try:
        body=request.get_json()
        input_data=body["data"].strip()
        if input_data=="" :
            return make_response(jsonify({"data":"Error in received payload"}),400)
        else:
            related_words = usernamecontroller(input_data)
            related_words=related_words.json
            return make_response(jsonify({"data": related_words}), 200)
    except Exception as e:
        return make_response(jsonify({"error":str(e)}),400)
    
@app.route(os.getenv("py_toxic_model_api_link"),methods=['POST'])
def toxicworddetection():
    try:
        body=request.get_json()
        input_data=body["data"].strip()
        if input_data=="" :
            return make_response(jsonify({"data":"Error in received payload"}),400)
        else:
             response=toxiccontroller(input_data)
             final_response=response.json[0]["label"]
             return make_response(jsonify({"data":final_response}), 200)
    except Exception as e:
        return make_response(jsonify({"error":str(e)}),400)
    

if __name__=="__main__":
    app.run(debug=True,port=os.getenv("py_port"))
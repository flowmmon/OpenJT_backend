from http import HTTPStatus  
from flask import Flask, request, jsonify  
from flask_cors import CORS
from dashscope import Application  
import os  

app = Flask(__name__)  

CORS(app) 

API_KEY ="sk-47fb69ec2b3141eeaf7ed46981433c53"

@app.route('/call_agent', methods=['POST'])  
def call_agent_app():  
    data = request.json  
    prompt = data.get('prompt')  

    if not prompt:  
        return jsonify({'error': 'Prompt is required'}), HTTPStatus.BAD_REQUEST  

    response = Application.call(app_id='19881d3703494ad5b2f8593d900e37a5',  
                                prompt=prompt,  
                                api_key=API_KEY)  

    if response.status_code != HTTPStatus.OK:  
        return jsonify({  
            'request_id': response.request_id,  
            'code': response.status_code,  
            'message': response.message  
        }), HTTPStatus.INTERNAL_SERVER_ERROR  
    else:  
        return jsonify({  
            'request_id': response.request_id,  
            'output': response.output,  
            'usage': response.usage  
        }), HTTPStatus.OK  

if __name__ == '__main__':  
    app.run(debug=True)
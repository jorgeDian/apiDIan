from flask import Flask, jsonify, request
import os
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def save_json():
    try:
        # Get the JSON data from the request
        json_data = request.json
        
        # Change the destination directory as per your requirement
        destination = os.path.join('uploads', 'data.json')
        
        # Save the JSON data to a file
        with open(destination, 'w') as file:
            json.dump(json_data, file)
        
        return jsonify({'message': 'JSON data saved successfully', 'path': destination})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/', methods=['GET'])
def get_json_data():
    try:
        # Change the destination directory as per your requirement
        destination = os.path.join('uploads', 'data.json')
        
        # Check if the file exists
        if os.path.exists(destination):
            # Read the JSON data from the file
            with open(destination, 'r') as file:
                json_data = json.load(file)
            
            return jsonify(json_data)
        else:
            return jsonify({'message': 'File not found'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

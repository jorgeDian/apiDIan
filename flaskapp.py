from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
CORS(app)

# Conexión a la base de datos MongoDB
client = MongoClient('mongodb+srv://camilo:bLnRuVtBKoXsczqd@cluster0.ffmtk6k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['Cluster0']  # Nombre de tu base de datos
collection = db['data']  # Nombre de tu colección

@app.route('/task', methods=['POST'])
def save_json():
    try:
        # Obtener los datos JSON de la solicitud
        json_data = request.json
        
        # Insertar los datos JSON en la colección de MongoDB
        result = collection.insert_one(json_data)
        
        return jsonify({'message': 'JSON data saved successfully', 'inserted_id': str(result.inserted_id)})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/task', methods=['GET'])
def get_json_data():
    try:
        # Obtener todos los documentos de la colección
        cursor = collection.find({})
        
        # Convertir los documentos a una lista de diccionarios
        json_data = [{**document, '_id': str(document['_id'])} for document in cursor]
        
        return jsonify(json_data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

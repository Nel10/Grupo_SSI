from flask import Flask, request, json, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo


app = Flask(__name__)
CORS(app)


app.config['MONGO_URI'] = 'mongodb+srv://cluster0.ccgqn.mongodb.net/myFirstDatabase'


mongo = PyMongo(app)

@app.route('/createPerson', methods=['POST'])
def createPerson():
    
    tipo_documento = request.json['tipo_documento']
    numero_documento= request.json['numero_documento']
    primer_nombre = request.json['primer_nombre']
    segundo_nombre = request.json['segundo_nombre']
    
    if tipo_documento and numero_documento and primer_nombre and segundo_nombre:
        objeto = mongo.db.person.insert_one({
            'tipo_documento': tipo_documento,
            'numero_documento': numero_documento,
            'primer_nombre': primer_nombre,
            'segundo_nombre': segundo_nombre
        })

        return jsonify({
            'data': {
                '_id': str(objeto.inserted_id),
                'tipo_documento': tipo_documento,
                'numero_documento': numero_documento,
                'primer_nombre': primer_nombre,
                'segundo_nombre': segundo_nombre
            },
            'message': 'Usuario ' + primer_nombre + ' agregado satisfactoriamente'
        }), 200
    else:
        return jsonify({'data': {}, 'message': 'Los campos tipo_documento, numero_documento, primer_nombre y segundo_nombre son obligatorios'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)

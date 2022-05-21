from copyreg import constructor
from telnetlib import TELNET_PORT
from urllib import response
from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
from datetime import datetime
from dateutil.relativedelta import relativedelta
from flask_cors import CORS

#biblioteca para guardar datos
#from werkzeug.security import generate_password_hash, check_password_hash

app=Flask(__name__)

#Base de datos
app.config['MONGO_URI']='mongodb+srv://sistemasfunkiduuh:Sistemas1234;@cluster0.i5lgt.mongodb.net/funkiduuhRegistro?retryWrites=true&w=majority'
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

mongo=PyMongo(app)

#ENDPOINT PARA TUTOR
#CrearTutor (Regresa el ID del tutor creado)
@app.route('/tutor', methods=['POST'])
def create_tutor():
    #Recibir los datos
    nombre=request.json['nombre']
    apellidoPaterno=request.json['apellidoPaterno']
    apellidoMaterno=request.json['apellidoMaterno']
    correo=request.json['correo']
    telPrincipal=request.json['telPrincipal']
    telSecundario=request.json['telSecundario']
    #Si el ususario me esta mandando todos sus datos se guardan en la base de datos
    if nombre and apellidoPaterno and apellidoMaterno and correo and telPrincipal and telSecundario:
        Tutor=mongo.db.tutor.insert_one(
            {
               'nombre':nombre,
               'apellidoPaterno':apellidoPaterno,
               'apellidoMaterno':apellidoMaterno,
               'correo':correo,
               'telPrincipal':telPrincipal,
               'telSecundario':telSecundario 
            }
        )
        response={
            '_id':str(Tutor.inserted_id)
        }
        return response
    #si no me manda todos sus datos un error    
    else:
        return not_found

#Obtener datos del tutor
@app.route('/tutor/<id>', methods=['GET'])
def get_tutor(id):
    tutor = mongo.db.tutor.find_one({'_id':ObjectId(id), })
    response = json_util.dumps(tutor)
    return Response(response, mimetype="application/json")

#Eliminar tutor
@app.route('/tutor/<id>', methods=['DELETE'])
def delete_tutor(id):
    mongo.db.tutor.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'Tutor Deleted Successfully'})
    response.status_code = 200
    return response

#Actualizar tutor
@app.route('/tutor/<_id>', methods=['PUT'])
def update_tutor(_id):
    #Recibir los datos
    nombre=request.json['nombre']
    apellidoPaterno=request.json['apellidoPaterno']
    apellidoMaterno=request.json['apellidoMaterno']
    correo=request.json['correo']
    telPrincipal=request.json['telPrincipal']
    telSecundario=request.json['telSecundario']
    #Si el ususario me esta mandando todos sus datos se guardan en la base de datos
    if nombre and apellidoPaterno and apellidoMaterno and correo and telPrincipal and telSecundario:
        mongo.db.tutor.update_one(
             {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set':{
                 'nombre':nombre,
                 'apellidoPaterno':apellidoPaterno,
                 'apellidoMaterno':apellidoMaterno,
                 'correo':correo,
                 'telPrincipal':telPrincipal,
                 'telSecundario':telSecundario
             }}
        )
        response = jsonify({'message': 'Tutor Updated Successfuly'})
        response.status_code = 200
        return response
    #si no me manda todos sus datos un error    
    else:
        return not_found

#ENDIPOINTS PARA MENOR
#CrearMenor (Recibe el ID del tutor a cargo)
@app.route('/menor/<_idTutor>', methods=['POST'])
def create_menor(_idTutor):
    #Recibir los datos
    primerNombre=request.json['primerNombre']
    segundoNombre=request.json['segundoNombre']
    apellidoPaterno=request.json['apellidoPaterno']
    apellidoMaterno=request.json['apellidoMaterno']
    fechaNacimiento=datetime.strptime(request.json['fechaNacimiento'], "%Y-%m-%d")
    edadAux = relativedelta(datetime.now(), fechaNacimiento)
    edad=edadAux.years
    #Si el ususario me esta mandando todos sus datos se guardan en la base de datos
    if primerNombre and apellidoPaterno and fechaNacimiento:
        Menor=mongo.db.menor.insert_one(
            {
               'primerNombre':primerNombre,
               'segundoNombre':segundoNombre,
               'apellidoPaterno':apellidoPaterno,
               'apellidoMaterno':apellidoMaterno,
               'fechaNacimiento':fechaNacimiento,
               'edad':edad,
               'idTutor':_idTutor
            }
        )
        response={
            '_id':str(Menor.inserted_id)
        }
        return response
    #si no me manda todos sus datos un error    
    else:
        return not_found

#Crear varios menores
@app.route('/menor/varios/<_idTutor>', methods=['POST'])
def create_menor_varios(_idTutor):
    list=[]
    #Recibir los datos
    for item in request.json:
        primerNombre=item['primerNombre']
        segundoNombre=item['segundoNombre']
        apellidoPaterno=item['apellidoPaterno']
        apellidoMaterno=item['apellidoMaterno']
        fechaNacimiento=datetime.strptime(item['fechaNacimiento'], "%Y/%m/%d")
        edadAux = relativedelta(datetime.now(), fechaNacimiento)
        edad=edadAux.years
        list.append({
            'primerNombre':primerNombre,
            'segundoNombre':segundoNombre,
            'apellidoPaterno':apellidoPaterno,
            'apellidoMaterno':apellidoMaterno,
            'fechaNacimiento':fechaNacimiento,
            'edad':edad,
            'idTutor':_idTutor
        })
    #Si el ususario me esta mandando todos sus datos se guardan en la base de datos
    if len(list)>0:
        mongo.db.menor.insert_many(list)
        response = jsonify({'message': 'Mennor Added Successfully'})
        return response
    #si no me manda todos sus datos un error    
    else:
        return not_found

#Obtener datos de 1 menor con el ID del menor
@app.route('/menor/<id>', methods=['GET'])
def get_menor(id):
    menor = mongo.db.menor.find_one({'_id':ObjectId(id), })
    response = json_util.dumps(menor)
    return Response(response, mimetype="application/json")

#Obtener datos de varios menores con el ID del tutor
@app.route('/menor/varios/<id>', methods=['GET'])
def get_menor_varios(id):
    menor = mongo.db.menor.find({'idTutor':id, })
    response = json_util.dumps(menor)
    return Response(response, mimetype="application/json")

#Eliminar menor
@app.route('/menor/<id>', methods=['DELETE'])
def delete_menor(id):
    mongo.db.menor.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'Menor Deleted Successfully'})
    response.status_code = 200
    return response

#Eliminar varios menores
@app.route('/menor/varios/<_idTutor>', methods=['DELETE'])
def delete_menor_varios(_idTutor):
    mongo.db.menor.delete_many({'idTutor': _idTutor})
    response = jsonify({'message': 'Menor Deleted Successfully'})
    response.status_code = 200
    return response

#Actualizar menor
@app.route('/menor/<_id>', methods=['PUT'])
def update_menor(_id):
    #Recibir los datos
    primerNombre=request.json['primerNombre']
    segundoNombre=request.json['segundoNombre']
    apellidoPaterno=request.json['apellidoPaterno']
    apellidoMaterno=request.json['apellidoMaterno']
    fechaNacimiento=datetime.strptime(request.json['fechaNacimiento'], "%Y-%m-%d")
    edadAux = relativedelta(datetime.now(), fechaNacimiento)
    edad=edadAux.years
    #Si el ususario me esta mandando todos sus datos se guardan en la base de datos
    if primerNombre and apellidoPaterno and fechaNacimiento:
        mongo.db.menor.update_one(
             {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set':{
                 'primerNombre':primerNombre,
                 'segundoNombre':segundoNombre,
                 'apellidoPaterno':apellidoPaterno,
                 'apellidoMaterno':apellidoMaterno,
                 'fechaNacimiento':fechaNacimiento,
                 'edad':edad,
             }}
        )
        response = jsonify({'message': 'Menor Updated Successfuly'})
        response.status_code = 200
        return response
    #si no me manda todos sus datos un error    
    else:
        return not_found

#Actualizar edad del menor
@app.route('/menor/edad/<_id>', methods=['PUT'])
def update_menor_edad(_id):
    #Recibir los datos
    menor = mongo.db.menor.find_one({'_id':ObjectId(_id), })
    fechaNacimiento=menor['fechaNacimiento']
    edadAux = relativedelta(datetime.now(), fechaNacimiento)
    edad=edadAux.years
    #Si el ususario me esta mandando todos sus datos se guardan en la base de datos
    if fechaNacimiento:
        mongo.db.menor.update_one(
             {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set':{
                 'edad':edad,
             }}
        )
        response = jsonify({'message': 'Menor Updated Successfuly'})
        response.status_code = 200
        return response
    #si no me manda todos sus datos un error    
    else:
        return not_found

#Por si ocurre un error en busquedas o url (hay que adaptarlo a la pagina)
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__=="__main__":
    app.run(debug=True);
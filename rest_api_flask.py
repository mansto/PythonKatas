# https://flask.palletsprojects.com/en/stable/installation/

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get('/hello')
def hello_world():
    return 'Hello, World!'

@app.get('/person/<int:id>')
def getPerson(id):
    return jsonify ({
        'id': id,
        'name': 'John Doe',
        'age': 25
    }), 201

@app.post('/person')
def add_person():
    data = request.get_json()
    if not data or not 'name' in data or not 'age' in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_person = {
        'id': data.get('id', 1),
        'name': data['name'],
        'age': data['age']
    }
    return jsonify(new_person), 201
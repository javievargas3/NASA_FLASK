from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Notes, notes_schema, note_schema


api = Blueprint('api', __name__, url_prefix='/api')
 

#Create
@api.route('/notes', methods = ['POST'])
@token_required
def create_Notes(current_user_token):
    date = request.json['comments']
    title = request.json['title']
    comments = request.json['comments']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')


    notes  = Notes(date, title, comments, user_token = user_token )

    db.session.add(notes)
    db.session.commit()

    response = note_schema.dump(notes)
    return jsonify(response)
#Read
@api.route('/notes', methods = ['GET'])
@token_required
def get_Notes(current_user_token):
    a_user = current_user_token.token
    notes = Notes.query.filter_by(user_token = a_user).all()
    response = notes_schema.dump(notes)
    return jsonify(response)
    

# UPDATE endpoint
@api.route('/notes/<id>', methods = ['POST','PUT'])
@token_required
def update_contact(current_user_token,id):
    notes = Notes.query.get(id) 
    notes.date = request.json['date']
    notes.title = request.json['title']
    notes.comments = request.json['comments']
    notes.user_token = current_user_token.token

    db.session.commit()
    response = note_schema.dump(notes)
    return jsonify(response)


# DELETE Notes ENDPOINT
@api.route('/notes/<id>', methods = ['DELETE'])
@token_required
def delete_Notes(current_user_token, id):
    notes = Notes.query.get(id)
    db.session.delete(notes)
    db.session.commit()
    response = note_schema.dump(notes)
    return jsonify(response)
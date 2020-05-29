from flask import jsonify, request
from flask_restful import Resource, reqparse
from models.user import User
import jwt
import datetime
import hashlib
from constants import SECRET_KEY

class Authentication(Resource):
    def post(self):
        json = request.get_json()
        user = User.query.filter_by(username=json["user"]).first()

        if( user != None and user.hash == hashlib.sha512((json["password"] + user.salt).encode('utf-8')).hexdigest()):
            
            token = jwt.encode({
                'exp' : datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'user' : user.username
            
            }, SECRET_KEY,  algorithm='HS256').decode('utf-8')            
            return {'token' : str(token)}
        else:
            return {'error' : 'username or password are not correct'}, 403
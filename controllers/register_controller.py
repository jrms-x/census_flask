from database.sqlalchemy import db
from models.user import User
from flask import jsonify, request
from flask_restful import reqparse, Resource
import hashlib, uuid


class Register(Resource):
    def post(self):
        json = request.get_json()
        username = json["user"]
        password = json["password"]

        foundUser = User.query.filter_by(username=username).first()

        if foundUser is not None:
            return {"message": "Username {0} already exists".format(username)}, 400

        user = User()
        user.username = username
        user.salt = uuid.uuid4().hex
        user.hash = hashlib.sha512((password + user.salt).encode('utf-8')).hexdigest()
        db.session.add(user)
        db.session.commit()
        return jsonify(message="User created")

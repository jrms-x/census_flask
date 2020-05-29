from flask import request, jsonify
from flask_restful import Resource, marshal, fields
from models.block import Block as BlockDB
from models.property import Property
from controllers.property_controller import properties_fields
from authentication.token_annotation import token_required
from database.sqlalchemy import db

block_fields = {
    "id": fields.Integer,
    "block_name": fields.String
}


class BlockProperties(Resource):
    @token_required
    def get(self, idBlock):
        return marshal(Property.query.filter_by(block=idBlock).all(), properties_fields), 200


class Block(Resource):
    @token_required
    def get(self, idBlock):
        block = BlockDB.query.filter_by(id=idBlock).first()
        if block is None:
            return {"message": "Block not found"}, 404
        else:
            return marshal(block, block_fields), 200


class BlockList(Resource):
    @token_required
    def post(self):
        json = request.get_json()
        blockFound = BlockDB.query.filter_by(id=json["id"]).first()
        if blockFound is not None:
            return jsonify(message="Id {0} already exists".format(json["id"]))
        newBlock = BlockDB()
        newBlock.id = json["id"],
        newBlock.block_name = json["block_name"]

        db.session.add(newBlock)
        db.session.commit()

        return jsonify(message="Block saved")

    @token_required
    def get(self):
        return marshal(BlockDB.query.all(), block_fields), 200

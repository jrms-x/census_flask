from flask import jsonify, request
from flask_restful import reqparse, Resource, marshal, fields
from authentication.token_annotation import token_required
from models.property import Property as PropertyDB
from database.sqlalchemy import db

properties_fields = {
    "id": fields.Integer,
    "block": fields.Integer,
    "property": fields.Integer,
    "derived": fields.Integer,
    "name": fields.String,
    "street": fields.String,
    "suburb": fields.String,
    "number": fields.String,
    "bis": fields.String,
    "interior": fields.String,
    "building": fields.String,
    "floor": fields.String,
    "block_city": fields.String,
    "lot": fields.String,
    "customer_rating": fields.String,
    "location": fields.String,
    "serial_number": fields.String,
    "type_service": fields.Integer
}


class Property(Resource):
    @token_required
    def get(self, idProperty):
        propertyFound = PropertyDB.query.filter_by(id=idProperty).first()
        if propertyFound is None:
            return {"message": "Property not found"}, 404
        else:
            return marshal(propertyFound, properties_fields), 200


class PropertyList(Resource):
    @token_required
    def get(self):
        return marshal(PropertyDB.query.all(), properties_fields), 200

    @token_required
    def post(self):
        newProperty = PropertyDB()
        json = request.get_json()
        newProperty.block = json.get("block")
        newProperty.property = json.get("property")
        newProperty.derived = json.get("derived")
        newProperty.name = json.get("name")
        newProperty.street = json.get("street")
        newProperty.suburb = json.get("suburb")
        newProperty.number = json.get("number")
        newProperty.bis = json.get("bis")
        newProperty.interior = json.get("interior")
        newProperty.building = json.get("building")
        newProperty.floor = json.get("floor")
        newProperty.block_city = json.get("block_city")
        newProperty.lot = json.get("lot")
        newProperty.customer_rating = json.get("customer_rating")
        newProperty.location = json.get("location")
        newProperty.serial_number = json.get("serial_number")
        newProperty.type_service = json.get("type_service")

        db.session.add(newProperty)
        db.session.commit()

        return jsonify(message="Property saved")

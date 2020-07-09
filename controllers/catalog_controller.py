from flask import request
from flask_restful import Resource, fields, marshal
from authentication.token_annotation import token_required
from models.catalog import Catalog
from database.sqlalchemy import db

catalog_fields = {
    "id" : fields.Integer,
    "name" : fields.String,
    "type" : fields.String
}

class CatalogList(Resource):
    @token_required
    def get(self):
        anomalies = marshal(Catalog.query.filter_by(type="ANOMALIES").all(), catalog_fields)
        meterStatus = marshal(Catalog.query.filter_by(type="METER_STATUS").all(), catalog_fields)
        meterBrands = marshal(Catalog.query.filter_by(type="METER_BRANDS").all(), catalog_fields)
        typesCharges = marshal(Catalog.query.filter_by(type="TYPES_CHARGES").all(), catalog_fields)
        typesProperties = marshal(Catalog.query.filter_by(type="TYPES_PROPERTIES").all(), catalog_fields)
        typesProtections = marshal(Catalog.query.filter_by(type="TYPES_PROTECTIONS").all(), catalog_fields)
        typesOutlet = marshal(Catalog.query.filter_by(type="TYPES_OUTLET").all(), catalog_fields)

        return {"anomalies" : anomalies, "meterStatus" : meterStatus, "meterBrands" : meterBrands, 
        "typesCharges" : typesCharges, "typesProperties" : typesProperties, 
        "typesProtections" : typesProtections, 
        "typesOutlet": typesOutlet}, 200
    
    @token_required
    def post(self):
        catalog = request.get_json()
        found_similar = Catalog.query.filter_by(name=catalog.get("name"), type=catalog.get("type")).first()
        if found_similar is not None:
            return {"message" : "Catalog found with name: {0} and type {1}".format(catalog.get("name"), catalog.get("type"))}, 400
        else:
            newCatalog = Catalog()
            newCatalog.name = get("name")
            newCatalog.type = get("type")
            db.session.add(newCatalog)
            db.session.commit()
            return {"message" : "Catalog added"}, 200

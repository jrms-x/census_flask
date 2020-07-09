from flask_restful import Resource, request
from models.census_data import CensusData as CensusDataDb
from database.sqlalchemy import db
from authentication.token_annotation import token_required

class CensusData(Resource):
    @token_required
    def post(self):
        json = request.get_json()
        foundCensus = CensusDataDb.query.filter_by(id_property=json.get("id_property")).first()
        if foundCensus is not None:
            return {"message" : "Census data already exists"}, 400
        census = self.__get_census_data_json(json)
        db.session.add(census)
        db.session.commit()
        return {"message" : "Census data added"}, 200
        
        
    
    def __get_census_data_json(self, json):
        census = CensusDataDb()
        census.id_anomaly = json.get("id_anomaly")
        census.id_meter_brands = json.get("id_meter_brands")
        census.id_meter_status = json.get("id_meter_status")
        census.id_property = json.get("id_property")
        census.id_type_charges = json.get("id_type_charges")
        census.id_type_properties = json.get("id_type_properties")
        census.id_type_protections = json.get("id_type_protections")
        census.id_type_outlet = json.get("id_type_outlet")
        census.year = json.get("year")
        
        return census
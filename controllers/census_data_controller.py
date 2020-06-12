from flask_restful import Resource, request
from models.census_data import CensusData as CensusDataDb
from database.sqlalchemy import db
from authentication.token_annotation import token_required

class CensusData(Resource):
    @token_required
    def post(self):
        json = request.get_json()
        foundCensus = CensusDataDb.query.filter_by(id_anomaly=json.get("anomalyID")).first()
        if foundCensus is not None:
            return {"message" : "Census data already exists"}, 400
        census = self.__get_census_data_json(json)
        db.session.add(census)
        db.session.commit()
        return {"message" : "Census data added"}, 200
        
        
    
    def __get_census_data_json(self, json):
        census = CensusDataDb()
        census.id = json.get("id")
        census.id_anomaly = json.get("anomalyID")
        census.id_meter_brands = json.get("meterBrandsID")
        census.id_meter_status = json.get("meterStatusID")
        census.id_property = json.get("propertyID")
        census.id_type_charges = json.get("typeChargesID")
        census.id_type_properties = json.get("typePropertiesID")
        census.id_type_protections = json.get("typeProtectionsID")
        census.id_type_outlet = json.get("typeOutletID")
        
        return census
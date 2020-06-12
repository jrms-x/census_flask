from database.sqlalchemy import db
from sqlalchemy import ForeignKey


class CensusData(db.Model):
    __tablename__ = "census_data"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    id_anomaly = db.Column(db.Integer, ForeignKey("catalogs.id"))
    id_meter_status = db.Column(db.Integer, ForeignKey("catalogs.id"))
    id_meter_brands = db.Column(db.Integer, ForeignKey("catalogs.id"))
    id_type_charges = db.Column(db.Integer, ForeignKey("catalogs.id"))
    id_type_properties = db.Column(db.Integer, ForeignKey("catalogs.id"))
    id_type_protections = db.Column(db.Integer, ForeignKey("catalogs.id"))
    id_type_outlet = db.Column(db.Integer, ForeignKey("catalogs.id"))

    id_property = db.Column(db.Integer, ForeignKey("properties.id"))

    property = db.relationship("Property", uselist=False, back_populates="census_data" )
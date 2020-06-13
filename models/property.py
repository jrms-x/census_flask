from database.sqlalchemy import db
from sqlalchemy import ForeignKey


class Property(db.Model):
    __tablename__ = "properties"
    id = db.Column(db.Integer, primary_key=True)
    block = db.Column(db.Integer, ForeignKey("blocks.id"), nullable=False)
    property = db.Column(db.Integer, nullable=False)
    derived = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    street = db.Column(db.String(256), nullable=False)
    suburb = db.Column(db.String(256), nullable=False)
    number = db.Column(db.String(64), nullable=False)
    bis = db.Column(db.String(64))
    interior = db.Column(db.String(64))
    building = db.Column(db.String(128))
    floor = db.Column(db.String(64))
    block_city = db.Column(db .String(128))
    lot = db.Column(db.String(64))
    customer_rating = db.Column(db.String(256), nullable=True)
    location = db.Column(db.String(256))
    serial_number = db.Column(db.String(64))
    type_service = db.Column(db.Integer)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)

    census_data = db.relationship("CensusData", uselist=False, back_populates="property" )

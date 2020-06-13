from database.sqlalchemy import db
from sqlalchemy import ForeignKey

class Picture(db.Model):
    __tablename__ = "pictures"
    id = db.Column(db.String(40), primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    subtitle = db.Column(db.String(64))
    description = db.Column(db.String(128))
    blob_identifier = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer, nullable=False)
    id_property = db.Column(db.Integer, ForeignKey("properties.id") ,nullable=False)
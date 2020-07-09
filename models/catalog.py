from database.sqlalchemy import db

class Catalog(db.Model):
    __tablename__ = "catalogs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    type = db.Column(db.String(64), nullable=False)

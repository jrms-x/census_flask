from database.sqlalchemy import db

class Block(db.Model):
    __tablename__ = "blocks"
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    block_name = db.Column(db.String(128), unique=True, nullable=False)
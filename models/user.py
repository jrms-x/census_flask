from database.sqlalchemy import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    salt = db.Column(db.String(255), nullable=False)
    hash = db.Column(db.Text, nullable=False)
from flask import Flask, g, request, redirect, url_for
from flask_restful import Resource, Api
from controllers.authenticate_controller import Authentication
from controllers.register_controller import Register
from controllers.property_controller import Property, PropertyList
from controllers.block_controller import Block, BlockList, BlockProperties
from database.sqlalchemy import db
from authentication.token_annotation import token_required
from constants import DATABASE_URL
from controllers.catalog_controller import CatalogList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

db.init_app(app)

with app.app_context():
    db.create_all()

app.url_map.strict_slashes = False

ws = Api(app)


@app.route("/")
@token_required
def test():
    hello = "hello world"
    return hello


ws.add_resource(Authentication, "/login")
ws.add_resource(Register, "/register")
ws.add_resource(PropertyList, "/properties/")
ws.add_resource(Property, "/properties/<int:idProperty>")
ws.add_resource(Block, "/blocks/<int:idBlock>")
ws.add_resource(BlockList, "/blocks/")
ws.add_resource(BlockProperties, "/blocks/<int:idBlock>/properties")
ws.add_resource(CatalogList, "/catalogs/")

if __name__ == '__main__':
    app.run(debug=True)

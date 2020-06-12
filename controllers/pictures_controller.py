from database.sqlalchemy import db
from flask_restful import Resource, request, fields, marshal, reqparse
from models.picture import Picture as PictureDB
from authentication.token_annotation import token_required
import uuid
import werkzeug

pictures_fileds = {
    "id" : fields.String,
    "title" : fields.String,
    "subtitle" : fields.String,
    "description" : fields.String,
    "location" : fields.String,
    "order" : fields.Integer,
    "id_property" : fields.Integer
}


class Picture(Resource):
    @token_required
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument("image", type=werkzeug.datastructures.FileStorage, location="files")
        args = parse.parse_args()
        print(args.get("image"))
        picture = PictureDB()
        picture.id = str(uuid.uuid4())
        picture.id_property = request.form.get("id_property")
        picture.title = request.form.get("title")
        picture.subtitle = request.form.get("subtitle")
        picture.description = request.form.get("description")
        picture.location = "test"
        picture.order = request.form.get("order")

        db.session.add(picture)
        db.session.commit()

        return {"message" : "Picture saved"}, 20

    @token_required
    def delete(self):
        json = request.get_json()
        id = json.get("id")
        if(id is None):
            return {"message" : "Must send picture Id"}, 400
        deleted = PictureDB.query.filter_by(id=id).delete()
        db.session.commit()
        return {"message" : "Pictures deleted: {0}".format(deleted)}


    

class PictureList(Resource):
    @token_required
    def get(self, idProperty):
        return marshal(PictureDB.query.
        filter_by(id_property=idProperty).all(), pictures_fileds), 200

    




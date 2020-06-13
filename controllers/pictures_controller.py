from database.sqlalchemy import db
from flask import send_file
from flask_restful import Resource, request, fields, marshal, reqparse
from models.picture import Picture as PictureDB
from authentication.token_annotation import token_required
import uuid
from werkzeug.datastructures import FileStorage
import io
from files.drive_helper import DriveHelper

pictures_fileds = {
    "id" : fields.String,
    "title" : fields.String,
    "subtitle" : fields.String,
    "description" : fields.String,
    "blob_identifier" : fields.String,
    "order" : fields.Integer,
    "id_property" : fields.Integer
}


class Picture(Resource):
    @token_required
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument("image", type=FileStorage, location="files")
        args = parse.parse_args()
        picture = PictureDB()
        picture.id = str(uuid.uuid4())
        picture.id_property = request.form.get("id_property")
        picture.title = request.form.get("title")
        picture.subtitle = request.form.get("subtitle")
        picture.description = request.form.get("description")
        picture.blob_identifier = DriveHelper().upload_file(args.get("image").stream, args.get("image").content_type, args.get("image").filename)
        picture.order = request.form.get("order")

        db.session.add(picture)
        db.session.commit()

        return {"message" : "Picture saved", "info" : picture.id}, 200

    @token_required
    def delete(self):
        json = request.get_json()
        id = json.get("id")
        if(id is None):
            return {"message" : "Must send picture Id"}, 400
        toDelete = PictureDB.query.filter_by(id=id).first()
        DriveHelper().delete_file(toDelete.blob_identifier)
        db.session.delete(toDelete)
        db.session.commit()
        return {"message" : "Picture deleted:"}, 200
    
    @token_required
    def get(self):
        id = request.args.get("id")
        bytes = DriveHelper().download_file(id)
        return send_file(io.BytesIO(bytes), as_attachment=True ,attachment_filename=id, mimetype="image/*")



    

class PictureList(Resource):
    @token_required
    def get(self, idProperty):
        return marshal(PictureDB.query.
        filter_by(id_property=idProperty).all(), pictures_fileds), 200

    




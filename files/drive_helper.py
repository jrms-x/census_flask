import os
import io
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload, MediaIoBaseDownload

class DriveHelper:

    def __init__(self):
        super().__init__()
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(fileDir,"credentials.json")
        self.service = build('drive', 'v3')

    def upload_file(self, io_stream, mime_type ,name):
        file_metadata = {"name": name}
        media = MediaIoBaseUpload(io_stream, mime_type, -1)
        return self.service.files().\
            create(body=file_metadata, media_body=media, fields='id').execute().get('id')
    
    def delete_file(self, id):
        self.service.files().delete(fileId=id).execute()

    def download_file(self, id):
        return self.service.files().get_media(fileId=id).execute()
        '''stream = io.BytesIO()
        media_download = MediaIoBaseDownload(stream, file_from_drive)
        finished = False
        while finished is not True:
            _, finished = media_download.next_chunk()
        return stream'''

from google import storage
from fastapi import UploadFile, File

class UploadService:
    def __init__(self):
        self.client = storage.Client(project="marketmint-489521")

    def upload_file(bucket_name: str, file:UploadFile = File(...)):
            return file.filename
            
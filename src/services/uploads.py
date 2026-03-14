from google.cloud import storage
from fastapi import UploadFile, File

class UploadService:
    def __init__(self):
         self.client = storage.Client(project="marketmint-489521")

    async def upload_file(self,bucket_name: str, file:UploadFile = File(...)):
            
            bucket = self.client.get_bucket(bucket_name)
            blob = bucket.blob(file.filename)
            await file.seek(0)
            blob.upload_from_file(file.file,content_type=file.content_type)    
            return f"https://storage.googleapis.com/{bucket_name}/{file.filename}"
            
            
            
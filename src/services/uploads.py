from google.cloud import storage
from fastapi import UploadFile, File
from typing import List
import uuid



class UploadService:
    def __init__(self):
         self.client = storage.Client(project="marketmint-489521")

    async def upload_file(self,bucket_name: str, files:List[UploadFile]):
               try:
                    uploaded_assets = []
                    for file in files:
                         unique_filename = f"{uuid.uuid4()}-{file.filename}"
                         bucket = self.client.get_bucket(bucket_name)
                         # for file in files:
                         blob = bucket.blob(unique_filename)
                         await file.seek(0)
                         blob.upload_from_file(file.file,content_type=file.content_type)    
                         uploaded_assets.append({"name":file.filename,"size":str(file.size),"tag":file.filename,"url":f"https://storage.googleapis.com/{bucket_name}/{file.filename}","file_format":file.content_type})
                    return uploaded_assets 
               except Exception as e:
                     print(f"GCS upload error {e}")
                     raise(e)
    
            
            
            
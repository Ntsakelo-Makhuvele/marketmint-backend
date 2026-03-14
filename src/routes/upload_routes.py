from fastapi import APIRouter,UploadFile,File,status
from fastapi.exceptions import HTTPException
from src.services.uploads import UploadService

upload_service = UploadService()
upload_router = APIRouter()

@upload_router.post('/')
async def upload_file(bucket_name: str,file:UploadFile=File(...)):
      result = await upload_service.upload_file(bucket_name=bucket_name,file=file)
      if result:
            return {"file_url":result}
      else:
          raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Something went wrong')

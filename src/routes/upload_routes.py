from fastapi import APIRouter,UploadFile,File,status, Depends
from fastapi.exceptions import HTTPException
from src.services.uploads import UploadService
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from src.services.brand import BrandService
from src.database.database import get_session
import uuid

brand_service = BrandService()
upload_service = UploadService()
upload_router = APIRouter()

@upload_router.post('/{bucket_name}')
async def upload_file(bucket_name: str,brand_uuid:uuid.UUID, category_uuid:uuid.UUID,files:List[UploadFile] = File(...),session:AsyncSession=Depends(get_session)):
      try:
            result = await upload_service.upload_file(bucket_name=bucket_name,files=files)
            if result:
                  for file in result:
                        await brand_service.create_brand_asset({"name":file["name"],"size":file["size"],"tag":file["tag"],"url":file["url"],"file_format":file["file_format"], "brand_uuid":brand_uuid,"category_uuid":category_uuid},session=session)
                  return result
            else:
              raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Something went wrong')
      except HTTPException as e:
              raise e 
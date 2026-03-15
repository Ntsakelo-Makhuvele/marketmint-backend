from fastapi import APIRouter, status, Depends, Response
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from src.services.brand import BrandService
from src.schemas.brand import BrandCreateRequest, BrandToneCreateRequest
from src.database.database import get_session
from sqlalchemy.exc import SQLAlchemyError
from src.models.brand import Brand
from typing import List

brand_router = APIRouter()
brand_service = BrandService()

@brand_router.post('/')
async def create_brand(data:BrandCreateRequest,session:AsyncSession = Depends(get_session)):
    try:
        
        result = await brand_service.create_brand(brand_data=data,session=session)
        if result is not None:
           return result[0]
        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="something went wrong") 
    except SQLAlchemyError as e:
          raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"{e}")

@brand_router.get('/')
async def get_brand(brand_uuid:str, session:AsyncSession = Depends(get_session)):
     try:
         result = await brand_service.get_brand(brand_uuid=brand_uuid, session=session) 
         return result
     except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"{e}")
     
@brand_router.post('/tone')
async def create_brand_tone(brand_tone_list: List[BrandToneCreateRequest],brand_uuid:str, session: AsyncSession = Depends(get_session)):
    try:
        result = await brand_service.create_brand_tone(brand_tone_list=brand_tone_list,brand_uuid=brand_uuid,session=session)
        if result is not None:
            return {"processed":result}
        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="something went wrong")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"{e}")
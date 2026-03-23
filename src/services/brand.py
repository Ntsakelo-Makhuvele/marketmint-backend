from sqlmodel.ext.asyncio.session import AsyncSession
from src.schemas.brand import BrandCreateRequest, BrandToneCreateRequest,BrandAssetCreateRequest
from src.models.brand import Brand, BrandTone, BrandAsset
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import select,delete
from typing import List
import uuid

class BrandService:
    async def create_brand(self,brand_data:BrandCreateRequest, session:AsyncSession):
        try:
            brand_data_dict = brand_data.model_dump()

            new_brand_data = Brand(
                **brand_data_dict
            )

            session.add(new_brand_data)

            session.commit()
            
            return brand_data_dict
        except SQLAlchemyError as e:
            print(e)   


    async def get_brand(self,brand_uuid:str, session:AsyncSession):
        try:
            statement = select(Brand).where(Brand.uuid == brand_uuid)
            result = session.execute(statement)
            brand = result.scalars().all()

            return brand if brand is not None else None  
        except SQLAlchemyError as e:
            print(e)
    
    async def create_brand_tone(self, brand_tone:BrandToneCreateRequest, brand_uuid:str, session:AsyncSession):
        try:            
                brand_tone_dict = brand_tone.model_dump()
                new_brand_tone = BrandTone(
                    **brand_tone_dict,
                    brand_uuid=brand_uuid
                )

                session.add(new_brand_tone)

                session.commit()

                return brand_tone
        except SQLAlchemyError as e:
            print(e)

    async def create_brand_asset(self,asset_data:BrandAssetCreateRequest, session:AsyncSession):
        try:
             #asset_data_dict = asset_data.model_dump()

             new_asset_data = BrandAsset(
                 **asset_data
             )

             session.add(new_asset_data)

             await session.commit()

             return asset_data   
        except SQLAlchemyError as e:
            print(e)

    async def get_brand_tone(self,tone_uuid:str, session:AsyncSession):
        try:
            statement = select(BrandTone).where(BrandTone.uuid==tone_uuid)
            result = session.execute(statement)
            tone = result.scalars().all()
            return tone if tone is not None else None
        except SQLAlchemyError as e:
            print(e)

    async def remove_brand_tone(self, tone_uuid:str, session:AsyncSession):
        try:
            statement = delete(BrandTone).where(BrandTone.uuid==tone_uuid).returning(BrandTone)
            result = session.execute(statement)
            removed_tone = result.scalars().all()
            session.commit()
            return removed_tone if removed_tone is not None else None
        except SQLAlchemyError as e:
            print(e)
 
    

    
    
   

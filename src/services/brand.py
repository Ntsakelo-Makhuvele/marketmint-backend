from sqlmodel.ext.asyncio.session import AsyncSession
from src.schemas.brand import BrandCreateRequest, BrandToneCreateRequest
from src.models.brand import Brand, BrandTone
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import select
from typing import List

class BrandService:
    async def create_brand(self,brand_data:BrandCreateRequest, session:AsyncSession):
        try:
            brand_data_dict = brand_data.model_dump()

            new_brand_data = Brand(
                **brand_data_dict
            )

            session.add(new_brand_data)

            await session.commit()
            
            return new_brand_data
        except SQLAlchemyError as e:
            print(e)   


    async def get_brand(self,brand_uuid:str, session:AsyncSession):
        try:
            statement = select(Brand).where(Brand.uuid == brand_uuid)
            result = await session.execute(statement)
            brand = result.scalars().all()

            return brand if brand is not None else None  
        except SQLAlchemyError as e:
            print(e)
    
    async def create_brand_tone(self, brand_tone_list:List[BrandToneCreateRequest], brand_uuid:str, session:AsyncSession):
        try:
            for brand_tone in brand_tone_list:
                brand_tone_dict = brand_tone.model_dump()
                new_brand_tone = BrandTone(
                    **brand_tone_dict,
                    brand_uuid=brand_uuid
                )

                session.add(new_brand_tone)

                await session.commit()

            return brand_tone_list
        except SQLAlchemyError as e:
            print(e)
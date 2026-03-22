# from sqlmodel import SQLModel, Field, Column, Relationship
# import sqlalchemy.dialects.postgresql as pg
# from datetime import datetime
# from typing import Optional, List
# from srcmodels.brand import Brand
# import uuid 


# class BrandAsset(SQLModel,table=True):
#     __tablename__ = 'brand_asset'

#     uuid: uuid.UUID = Field(
#       sa_column=Column(
#           pg.UUID,
#           nullable=False,
#           primary_key=True,
#           default=uuid.uuid4
#       ) 
#     )

#     name: str
#     tag: str
#     category_uuid: str = Field(foreign_key="asset_category.uuid")
#     url: str
#     brand_uuid: uuid.UUID = Field(foreign_key="brand.uuid") 
#     category_uuid: uuid.UUID = Field(foreign_key="asset_category.uuid")
#     brand: Optional[Brand] = Relationship(back_populates="assets")
#     category: Optional[AssetCategory] = Relationship(back_populates="assets")

    

# class AssetCategory(SQLModel,table=True):
#     __tablename__ = 'asset_category'
    
#     uuid: uuid.UUID = Field(
#       sa_column=Column(
#           pg.UUID,
#           nullable=False,
#           primary_key=True,
#           default=uuid.uuid4
#       ) 
#     )

#     name: str
#     description: str
#     assets: List["BrandAsset"] = Relationship(back_populates="category")
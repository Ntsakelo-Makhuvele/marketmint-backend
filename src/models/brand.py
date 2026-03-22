from sqlmodel import SQLModel, Field, Column, Relationship
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
import uuid 
from typing import List, Optional

class Brand(SQLModel,table=True):
    __tablename__ = "brand"
    
    uuid: uuid.UUID = Field(
      sa_column=Column(
          pg.UUID,
          nullable=False,
          primary_key=True,
          default=uuid.uuid4
      ) 
    )

    creator_id: str 
    name: str
    description: str
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP,  default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP,  default=datetime.now, onupdate=datetime.now))
    brand_tones: List["BrandTone"] = Relationship(back_populates="brand")
    assets: List["BrandAsset"] = Relationship(back_populates="brand") 
    
    def __repr__(self):
        return f"<Brand {self.name}>"
    
class BrandTone(SQLModel, table=True):
    __tablename__ = "brand_tone"
    
    uuid: uuid.UUID = Field(
      sa_column=Column(
          pg.UUID(as_uuid=True),
          nullable=False,
          primary_key=True,
          default=uuid.uuid4
      ) 
    )

    brand_uuid: uuid.UUID = Field(foreign_key="brand.uuid")
    name: str
    target_audience: str
    brand_attributes: List[str] = Field(sa_column=Column(pg.ARRAY(pg.TEXT)))
    forbidden_words: List[str] = Field(sa_column=Column(pg.ARRAY(pg.TEXT)))
    system_instructions: str
    brand_primary_color: str
    aesthetics: str
    music_pacing: str
    brand: Optional[Brand] = Relationship(back_populates="brand_tones")
    
    def __repr__(self):
        return f"<Tone {self.name}>"
    

class BrandAsset(SQLModel,table=True):
    __tablename__ = 'brand_asset'

    uuid: uuid.UUID = Field(
      sa_column=Column(
          pg.UUID,
          nullable=False,
          primary_key=True,
          default=uuid.uuid4
      ) 
    )

    name: str
    tag: str
    url: str
    size: str
    file_format: str
    brand_uuid: uuid.UUID = Field(foreign_key="brand.uuid") 
    category_uuid: uuid.UUID = Field(foreign_key="asset_category.uuid")
    brand: Optional[Brand] = Relationship(back_populates="assets")
    category: Optional[AssetCategory] = Relationship(back_populates="assets")

    def __repr__(self):
       return f"<BrandAsset {self.name}>"

    

class AssetCategory(SQLModel,table=True):
    __tablename__ = 'asset_category'
    
    uuid: uuid.UUID = Field(
      sa_column=Column(
          pg.UUID,
          nullable=False,
          primary_key=True,
          default=uuid.uuid4
      ) 
    )

    name: str
    description: str
    assets: List["BrandAsset"] = Relationship(back_populates="category")

    def __repr__(self):
      return f"<AssetCategory {self.name}>"
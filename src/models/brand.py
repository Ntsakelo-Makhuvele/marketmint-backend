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

    user_id: str = Field(index=True)
    name: str
    description: str
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP,  default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP,  default=datetime.now, onupdate=datetime.now))
    brand_tones: List["BrandTone"] = Relationship(back_populates="brand")
    
    def __repr__(self):
        return f"<Brand {self.name}>"
    
class BrandTone(SQLModel, table=True):
    __tablename__ = "brand_tone"
    
    uuid: uuid.UUID = Field(
      sa_column=Column(
          pg.UUID,
          nullable=False,
          primary_key=True,
          default=uuid.uuid4
      ) 
    )

    brand_uuid: uuid.UUID = Field(foreign_key="brand.uuid")
    name: str
    brand: Optional[Brand] = Relationship(back_populates="brand_tones")
    
    def __repr__(self):
        return f"<Tone {self.name}>"
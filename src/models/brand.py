from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
import uuid 

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
    name: str
    description: str
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP,  default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP,  default=datetime.now))

    def __repr__(self):
        return f"<Brand {self.name}>"
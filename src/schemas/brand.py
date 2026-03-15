from pydantic import BaseModel 
from typing import Optional, List
from  src.models import BrandTone

class BrandCreateRequest(BaseModel):
    name: str
    description: str
    user_id: str 
    brand_tone: Optional[List[BrandTone]] = None

class BrandToneCreateRequest(BaseModel):
    name: str    
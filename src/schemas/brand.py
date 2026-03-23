from pydantic import BaseModel 
from typing import Optional, List
from  src.models import BrandTone
import uuid

class BrandCreateRequest(BaseModel):
    name: str
    description: str
    creator_id: str 
    brand_tone: Optional[List[BrandTone]] = None

class BrandToneCreateRequest(BaseModel):
    name: str 
    target_audience: str
    brand_attributes: List[str] 
    forbidden_words: List[str] 
    system_instructions: str
    brand_primary_color: str
    aesthetics: str
    music_pacing: str  

class BrandAssetCreateRequest(BaseModel):
    name: str
    tag: str
    url: str
    size: str
    file_format: str
    brand_uuid: uuid.UUID 
    category_uuid: uuid.UUID 
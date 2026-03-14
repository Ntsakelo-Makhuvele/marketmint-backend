from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional

class CampaignCreateRequest(BaseModel):
    id: int
    name: str
    description: str
    start_date: str
    end_date: str

class MarketMintOutput(BaseModel):
    campaign_id: str
    email_content: Optional[str] = None
    video_url: Optional[HttpUrl] = None
    image_creatives: Optional[List[HttpUrl]] = []
    status: str = "processing"


class CampaignAssets(BaseModel):
    # The actual content for the user
    email_body: str = Field(..., description="Full HTML or Markdown email copy with a clear CTA.")
    sms_copy: str = Field(..., description="A punchy SMS under 160 characters including emojis.")
    
    # The 'instructions' for your other AI models
    video_generation_prompt: str = Field(
        ..., 
        description="A detailed, cinematic prompt for Google Veo. Describe lighting, motion, and subject."
    )
    image_generation_prompt: str = Field(
        ..., 
        description="A descriptive prompt for Imagen 3 to create a matching high-res social graphic."
    )
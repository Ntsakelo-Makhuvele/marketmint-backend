from fastapi import APIRouter
from src.services.campaign import CampaignService
#from src.models.campaign_model import CampaignCreateRequest
from src.schemas.campaign import CampaignCreateRequest

campaign_service = CampaignService()
campaign_router = APIRouter()

@campaign_router.post('/email')
async def create_email_campaign(campaign_data: CampaignCreateRequest):
    result = campaign_service.create_email_campaign(campaign_data)
    
    if result:
        video_result = campaign_service.create_video(result.video_generation_prompt)

    return {"email_campaign": result,video_result: video_result}
    




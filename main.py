from fastapi import FastAPI
from src.routes.campaign_routes import campaign_router

app = FastAPI(title="Market Mint API", description="API for Market Mint application", version="1.0.0")


#app.include_router(router=create_email_campaign, prefix="/v1/campaign", tags=["Campaign"])
app.include_router(campaign_router, prefix="/v1/campaign", tags=["Campaign"])
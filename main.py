from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.routes.campaign_routes import campaign_router
from src.routes.upload_routes import upload_router
from src.database.database import engine # Import the engine directly
from src.routes.brand import brand_router
from src.database.database import init_db
import sqlalchemy

from sqlmodel import SQLModel

@asynccontextmanager
async def life_span(app: FastAPI):
       print(f"server is starting...")
       try:
          await init_db()
          print(f"Database initialized succesfully")  
       except Exception as e:
             print(f"Database initialization failed: {e}")    
       yield 
       print(f"server has been stopped")

app = FastAPI(title="Market Mint API", 
              description="API for Market Mint application", 
              version="1.0.0",
              lifespan=life_span
              )


app.include_router(campaign_router, prefix="/v1/campaign", tags=["Campaign"])
app.include_router(upload_router, prefix='/v1/upload', tags=["Upload"])
app.include_router(brand_router, prefix="/v1/brand", tags=["Brand"])
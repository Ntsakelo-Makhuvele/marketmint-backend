from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.core.config import Config

engine = AsyncEngine(
    create_engine(
    url=Config.DATABASE_URL,
    echo=True
    ))

async def init_db():
    async with  engine.begin() as conn:
        from src.models.brand import Brand

        await conn.run_sync(SQLModel.metadata.create_all)

        




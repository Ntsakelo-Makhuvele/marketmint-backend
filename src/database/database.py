from sqlmodel import  SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from src.core.config import Config

engine = create_async_engine(
    url=Config.DATABASE_URL,
    echo=True,
    connect_args={
        "command_timeout": 60,
        "ssl":"prefer"
    }
    )

async def init_db():
    async with  engine.begin() as conn:
        from src.models.brand import Brand

        await conn.run_sync(SQLModel.metadata.create_all)

        




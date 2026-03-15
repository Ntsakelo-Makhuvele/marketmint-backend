from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
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

async def get_session() -> AsyncSession:
    Session = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with Session() as session:
        yield session




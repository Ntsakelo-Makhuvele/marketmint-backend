from sqlmodel import text,Session, create_engine
from src.core.config import Config

engine = create_engine(
    url=Config.DATABASE_URL,
    echo=True
    )

def init_db():
    with  engine.begin() as conn:
      conn.execute(text("SELECT 1"))

def get_session() :
    with Session(engine) as session:
        yield session




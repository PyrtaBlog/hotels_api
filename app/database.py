from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

DB_URL = settings.get_sqlalchemy_dsn()

engine = create_async_engine(DB_URL)

async_session = sessionmaker(bind=engine, class_=AsyncSession , expire_on_commit=False)


class Base(DeclarativeBase):
    pass

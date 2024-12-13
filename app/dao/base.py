from sqlalchemy import select, insert

from app.database import async_session

class BaseDao:
    model = None
    
    @classmethod
    async def find_by_id(cls, id: int):
        async with async_session() as session:
            query = select(cls.model).filter_by(id=id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
            
    
    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()
            
    
    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def add(cls, **data):
        async with async_session() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
    
    
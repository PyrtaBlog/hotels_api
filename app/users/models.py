from sqlalchemy import Column, Integer, LargeBinary, String
from app.database import Base

class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    hashed_password = Column(LargeBinary, nullable=False)
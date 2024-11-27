from sqlalchemy import JSON, Column, ForeignKey, Integer, String
from app.database import Base

class Rooms(Base):
    __tablename__ = 'rooms'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_id = Column(ForeignKey("hotels.id", ondelete="CASCADE"))
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    services = Column(JSON)
    quantity = Column(Integer)
    image_id = Column(Integer)
from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Boolean

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Integer, default=1)
    is_admin = Column(Boolean, default=False)


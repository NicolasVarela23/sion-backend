from sqlalchemy import Column, Integer, String, Text, Boolean
from database import Base

class Clase(Base):
    __tablename__ = "clases"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    descripcion = Column(Text)
    url_video = Column(String(255))
    habilitada = Column(Boolean, default=False)
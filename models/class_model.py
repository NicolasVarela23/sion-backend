from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Clase(Base):
    __tablename__ = "clases"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    descripcion = Column(String(500))
    orden = Column(Integer, nullable=False, unique=True)
    habilitada = Column(Boolean, default=False)


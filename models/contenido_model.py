from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Contenido(Base):
    __tablename__ = "contenidos"

    id = Column(Integer, primary_key=True, index=True)
    clase_id = Column(Integer, ForeignKey("clases.id"), nullable=False)
    tipo = Column(String(50))  # Ej: "video", "pdf", "enlace"
    titulo = Column(String(255), nullable=False)
    url = Column(String(500), nullable=False)
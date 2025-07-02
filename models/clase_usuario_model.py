from sqlalchemy import Column, Integer, ForeignKey
from database import Base

class ClaseUsuario(Base):
    __tablename__ = "clases_habilitadas"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("usuarios.id"))
    clase_id = Column(Integer, ForeignKey("clases.id"))
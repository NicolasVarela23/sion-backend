from sqlalchemy import Column, Integer, ForeignKey
from database import Base

class UsuarioClase(Base):
    __tablename__ = "usuarios_clases"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    clase_id = Column(Integer, ForeignKey("clases.id"))
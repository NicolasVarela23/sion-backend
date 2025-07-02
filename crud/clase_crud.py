from sqlalchemy.orm import Session
from models.clase_model import Clase
from models.clase_usuario_model import ClaseUsuario

def crear_clase(db: Session, clase_data):
    nueva_clase = Clase(**clase_data.dict())
    db.add(nueva_clase)
    db.commit()
    db.refresh(nueva_clase)
    return nueva_clase

def habilitar_clase_para_usuario(db: Session, clase_id: int, user_id: int):
    relacion = ClaseUsuario(clase_id=clase_id, user_id=user_id)
    db.add(relacion)
    db.commit()
    return relacion

def obtener_clases_usuario(db: Session, user_id: int):
    return db.query(Clase).join(ClaseUsuario).filter(ClaseUsuario.user_id == user_id).all()
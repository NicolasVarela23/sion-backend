from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.contenido_model import Contenido
from models.class_model import Clase
from models.user_model import User
from routers.auth_router import get_current_user

router = APIRouter(prefix="/contenido", tags=["Contenido"])

@router.post("/")
def agregar_contenido_a_clase(
    clase_id: int,
    tipo: str,
    titulo: str,
    url: str,
    db: Session = Depends(get_db),
    usuario_actual: User = Depends(get_current_user)
):
    if not usuario_actual.is_admin:
        raise HTTPException(status_code=403, detail="No tienes permisos para agregar contenido")

    clase = db.query(Clase).filter_by(id=clase_id).first()
    if not clase:
        raise HTTPException(status_code=404, detail="Clase no encontrada")

    nuevo_contenido = Contenido(clase_id=clase_id, tipo=tipo, titulo=titulo, url=url)
    db.add(nuevo_contenido)
    db.commit()
    return {"mensaje": "Contenido agregado correctamente"}

@router.get("/por-clase/{clase_id}")
def obtener_contenido_de_clase(
    clase_id: int,
    db: Session = Depends(get_db),
    usuario_actual: User = Depends(get_current_user)
):
    # Validar acceso a la clase
    from models.clase_usuario_model import ClaseUsuario
    acceso = db.query(ClaseUsuario).filter_by(clase_id=clase_id, usuario_id=usuario_actual.id).first()
    if not acceso and not usuario_actual.is_admin:
        raise HTTPException(status_code=403, detail="No tienes acceso a esta clase")

    contenidos = db.query(Contenido).filter_by(clase_id=clase_id).all()
    return contenidos
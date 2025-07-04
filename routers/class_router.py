from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.class_model import Clase
from models.user_class_model import UsuarioClase
from models.user_model import User
from schemas.class_schema import ClaseCreate, ClaseResponse, ClaseOut
from routers.auth_router import get_current_user
from typing import List


router = APIRouter()

@router.post("/clases/", response_model=ClaseResponse)
def crear_clase(clase_data: ClaseCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Solo el administrador puede crear clases.")

    nueva_clase = Clase(**clase_data.dict())
    db.add(nueva_clase)
    db.commit()
    db.refresh(nueva_clase)
    return nueva_clase

@router.post("/clases/{clase_id}/habilitar/{user_id}")
def habilitar_clase(clase_id: int, user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Solo el administrador puede habilitar clases.")

    ya_asignada = db.query(UsuarioClase).filter_by(user_id=user_id, clase_id=clase_id).first()
    if ya_asignada:
        raise HTTPException(status_code=400, detail="Ya se asignó esta clase a ese usuario.")

    nueva_relacion = UsuarioClase(user_id=user_id, clase_id=clase_id)
    db.add(nueva_relacion)
    db.commit()
    return {"mensaje": "Clase habilitada para el usuario."}

@router.get("/mis-clases", response_model=list[ClaseResponse])
def obtener_mis_clases(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    clases = db.query(Clase)\
        .join(UsuarioClase, Clase.id == UsuarioClase.clase_id)\
        .filter(UsuarioClase.user_id == current_user.id, Clase.habilitada == True).all()
    return clases


@router.get("/mis-clases", response_model=List[ClaseOut])
def obtener_clases_del_usuario(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    clases_ids = db.query(UsuarioClase.clase_id).filter(
        UsuarioClase.user_id == current_user.id
    ).subquery()

    clases = db.query(Clase).filter(
        Clase.id.in_(clases_ids),
        Clase.habilitada == True
    ).all()

    return clases
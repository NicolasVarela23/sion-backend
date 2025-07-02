from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.class_model import Clase
from models.user_class_model import UserClase
from models.user_model import User
from schemas.class_schema import ClaseCreate, ClaseResponse
from routers.auth_router import get_current_user

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

    ya_asignada = db.query(UserClase).filter_by(user_id=user_id, clase_id=clase_id).first()
    if ya_asignada:
        raise HTTPException(status_code=400, detail="Ya se asignó esta clase a ese usuario.")

    nueva_relacion = UserClase(user_id=user_id, clase_id=clase_id)
    db.add(nueva_relacion)
    db.commit()
    return {"mensaje": "Clase habilitada para el usuario."}

@router.get("/mis-clases", response_model=list[ClaseResponse])
def obtener_mis_clases(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    clases = db.query(Clase)\
        .join(UserClase, Clase.id == UserClase.clase_id)\
        .filter(UserClase.user_id == current_user.id, Clase.habilitada == True).all()
    return clases
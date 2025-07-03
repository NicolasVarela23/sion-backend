from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.user_class_model import UsuarioClase
from schemas.user_class_schema import AsignacionClase, AsignacionClaseOut
from routers.auth_router import get_current_user
from models.user_model import User

router = APIRouter(prefix="/asignacion", tags=["Asignación de Clases"])

@router.post("/", response_model=AsignacionClaseOut)
def asignar_clase(asignacion: AsignacionClase, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Solo el admin puede asignar clases")

    db_asignacion = UsuarioClase(**asignacion.dict())
    db.add(db_asignacion)
    db.commit()
    db.refresh(db_asignacion)
    return db_asignacion
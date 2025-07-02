from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.clase_schema import ClaseCreate, ClaseResponse
from crud import clase_crud
from deps import get_current_user, admin_required
from routers.auth_router import get_current_user

router = APIRouter()

@router.post("/clases/", response_model=ClaseResponse)
def crear_clase(clase: ClaseCreate, db: Session = Depends(get_db), admin=Depends(admin_required)):
    return clase_crud.crear_clase(db, clase)

@router.post("/clases/{clase_id}/habilitar/{user_id}")
def habilitar_clase(clase_id: int, user_id: int, db: Session = Depends(get_db), admin=Depends(admin_required)):
    return clase_crud.habilitar_clase_para_usuario(db, clase_id, user_id)

@router.get("/mis-clases", response_model=list[ClaseResponse])
def mis_clases(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return clase_crud.obtener_clases_usuario(db, user.id)
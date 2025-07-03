from pydantic import BaseModel

class AsignacionClase(BaseModel):
    user_id: int
    clase_id: int

class AsignacionClaseOut(AsignacionClase):
    id: int

    class Config:
        from_attributes = True
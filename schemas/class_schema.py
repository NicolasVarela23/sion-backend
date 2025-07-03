from pydantic import BaseModel

class ClaseBase(BaseModel):
    titulo: str
    descripcion: str
    orden: int

class ClaseCreate(ClaseBase):
    pass

class ClaseResponse(ClaseBase):
    id: int
    habilitada: bool

    class Config:
        from_attributes = True

class ClaseOut(BaseModel):
    id: int
    titulo: str
    descripcion: str
    orden: int
    habilitada: bool

    class Config:
        from_attributes = True
from pydantic import BaseModel

class ClaseBase(BaseModel):
    titulo: str
    descripcion: str | None = None
    url_video: str | None = None

class ClaseCreate(ClaseBase):
    pass

class ClaseResponse(ClaseBase):
    id: int
    habilitada: bool

    class Config:
        from_attributes = True
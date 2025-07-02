from fastapi import FastAPI
from routers import auth_router
from database import engine, Base
from routers import class_router

app = FastAPI()

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)



app.include_router(auth_router.router)
app.include_router(class_router.router)
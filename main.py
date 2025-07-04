from fastapi import FastAPI
from routers import auth_router
from database import engine, Base
from routers import class_router
from routers import user_class_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Lista de orígenes permitidos (puedes poner "*" para permitir todos)
origins = [
    "http://127.0.0.1:5500"  # tu frontend (React, jQuery, etc.)
    
]
 
# Agregar el middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # or ["*"] para todos
    allow_credentials=False,
    allow_methods=["*"],              # ["GET", "POST", ...]
    allow_headers=["*"],              # ["Content-Type", "Authorization", ...]
)
# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)



app.include_router(auth_router.router)
app.include_router(class_router.router)
app.include_router(user_class_router.router)
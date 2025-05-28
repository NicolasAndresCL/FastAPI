from fastapi import FastAPI
import uvicorn
from app.routers import user
from app.db.database import Base, engine
from app.db import models  # Asegura la carga del modelo para crear tablas

# Crear tablas al iniciar
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

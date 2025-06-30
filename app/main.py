from fastapi import FastAPI
import uvicorn
from app.routers import user
from app.db.database import Base, engine
from app.db import models  # Asegura la carga del modelo para crear tablas
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

# Crear tablas al iniciar
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError):
    return JSONResponse(
        status_code=400,
        content={"detail": "Conflicto en base de datos: posible duplicado o violación de clave foránea"}
    )

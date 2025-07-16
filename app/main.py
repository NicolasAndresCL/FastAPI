from sqladmin import Admin, ModelView
from fastapi import FastAPI
import uvicorn
from app.routers import user
from app.db.database import Base, engine
from app.db import models  # Asegura la carga del modelo para crear tablas
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from fastapi.responses import RedirectResponse
from app.db.models import User      # Importa tu modelo User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.nombre, User.apellido, User.direccion, User.telefono, User.correo, User.creacion, User.estado]
# Crear tablas al iniciar
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user.router)

admin = Admin(app, engine)
admin.add_view(UserAdmin)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

# Redireccionar automáticamente a Swagger UI
@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError):
    return JSONResponse(
        status_code=400,
        content={"detail": "Conflicto en base de datos: posible duplicado o violación de clave foránea"}
    )

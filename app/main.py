from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse
from sqlalchemy.exc import IntegrityError
from sqladmin import Admin, ModelView
import uvicorn

from app.db import models
from app.db.database import engine
from app.routers import users_router

def create_app() -> FastAPI:
    app = FastAPI(title="FastAPI + MySQL + Alembic")

    # ⚠️ QUITAR Base.metadata.create_all -> usar Alembic para migraciones
    app.include_router(users_router)

    class UserAdmin(ModelView, model=models.User):
        column_list = [c.name for c in models.User.__table__.columns]

    admin = Admin(app, engine)
    admin.add_view(UserAdmin)

    @app.get("/", include_in_schema=False)
    async def redirect_to_docs():
        return RedirectResponse(url="/docs")

    @app.exception_handler(IntegrityError)
    async def integrity_error_handler(request: Request, exc: IntegrityError):
        return JSONResponse(
            status_code=400,
            content={"detail": "Conflicto en base de datos: posible duplicado o violación de clave foránea"}
        )

    return app

if __name__ == "__main__":
    uvicorn.run("app.main:create_app", port=8000, reload=True)

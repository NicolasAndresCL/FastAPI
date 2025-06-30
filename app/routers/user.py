# app/routers/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import UserCreate, UserRead
from app.db.database import get_db
from app.repository import user as user_repo

router = APIRouter(prefix="/user", tags=["Users"])

@router.get("/", response_model=list[UserRead])
def obtener_usuarios(db: Session = Depends(get_db)):
    return user_repo.get_all_users(db)

@router.get("/{user_id}", response_model=UserRead)
def obtener_usuario(user_id: int, db: Session = Depends(get_db)):
    user = user_repo.get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.post("/", response_model=UserRead)
def crear_usuario(user: UserCreate, db: Session = Depends(get_db)):
    if len(user.nombre) < 3:
        raise HTTPException(
            status_code=422,
            detail={
                "msg": "Nombre de usuario demasiado corto",
                "code": "USERNAME_TOO_SHORT"
            }
        )
    
    return user_repo.create_user(user, db)

@router.put("/{user_id}", response_model=UserRead)
def actualizar_usuario(user_id: int, updated_user: UserCreate, db: Session = Depends(get_db)):
    user = user_repo.get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user_repo.update_user(user, updated_user, db)

@router.delete("/{user_id}")
def eliminar_usuario(user_id: int, db: Session = Depends(get_db)):
    user = user_repo.get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    user_repo.delete_user(user, db)
    return {"respuesta": "Usuario eliminado correctamente"}

from fastapi import APIRouter
from app.schemas import User, UserId

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

usuarios = []
# This is a FastAPI router for managing users with CRUD operations.
# It includes endpoints to create, read, update, and delete users,
@router.get("/ruta1")
def ruta1():
    return {"mensaje": "Hola a todos, que tengas buenos días!"}

@router.get("/")
def obtener_usuarios():
    return {"usuarios": usuarios}

@router.post("/")
def crear_usuario(user:User):
    usuario= user.dict()
    usuarios.append(usuario)
    print(usuario)
    return {"Respuesta": "Usuario creado correctamente" }

@router.get("/{user_id}")
def obtener_usuario(user_id: int):
    for user in usuarios:
        if user["id"] == user_id:
            return {"user": user}
    return {"Error": "Usuario no encontrado"}

@router.post("/ObtenerUsuario")
def obtener_usuario2(user_id: UserId):
    for user in usuarios:
        if user["id"] == user_id:
            return {"user": user}
    return {"Error": "Usuario no encontrado"}

@router.delete("/{user_id}")
def eliminar_usuario(user_id: int):
    global usuarios
    usuarios = [user for user in usuarios if user["id"] != user_id]
    return {"Respuesta": "Usuario eliminado correctamente"}

@router.put("/{user_id}")
def actualizar_usuario(user_id: int,updated_user: User):
    for index, user in enumerate(usuarios):
        if user["id"] == user_id:
            usuarios[index]["id"] = updated_user.dict()["id"]
            usuarios[index]["nombre"] = updated_user.dict()["nombre"]
            usuarios[index]["apellido"] = updated_user.dict()["apellido"]
            usuarios[index]["direccion"] = updated_user.dict().get("direccion", user["direccion"])
            usuarios[index]["telefono"] = updated_user.dict().get("telefono", user["telefono"])
            return {"Respuesta": "Usuario actualizado correctamente"}
    return {"Error": "Usuario no encontrado"}
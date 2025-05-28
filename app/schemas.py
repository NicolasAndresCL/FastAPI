from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    nombre: str
    apellido: str
    direccion: Optional[str] = None
    telefono: int
    correo: EmailStr

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    creacion: datetime
    estado: bool

    model_config = {
        "from_attributes": True  # Para Pydantic v2
    }


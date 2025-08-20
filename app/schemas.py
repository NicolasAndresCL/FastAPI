from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    nombre: str = Field(..., min_length=3)
    apellido: str
    direccion: Optional[str] = None
    telefono: Optional[str] = Field(None, pattern=r"^\+?\d{7,15}$")
    correo: EmailStr

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=3)
    apellido: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = Field(None, pattern=r"^\+?\d{7,15}$")
    correo: Optional[EmailStr] = None

class UserRead(UserBase):
    id: int
    creacion: datetime
    estado: bool

    model_config = {"from_attributes": True}  # Pydantic v2

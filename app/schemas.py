from pydantic import BaseModel
from datetime import datetime
from typing import Optional
# User Model
class User(BaseModel): #schema
    id: int
    name: str
    apellido: str
    direccion: Optional[str]
    telefono: Optional[int]
    creacion_user: datetime = datetime.now()

class UserId(BaseModel):
    id: int
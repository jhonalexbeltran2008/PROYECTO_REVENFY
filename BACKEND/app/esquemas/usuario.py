from datetime import datetime
from pydantic import BaseModel, EmailStr


class UsuarioCrear(BaseModel):

    nombre: str

    apellido: str

    correo: EmailStr

    telefono: str

    programa_formacion: str


class UsuarioActualizar(BaseModel):

    nombre: str | None = None

    apellido: str | None = None

    telefono: str | None = None

    programa_formacion: str | None = None

    estado: bool | None = None


class UsuarioRespuesta(BaseModel):

    id_usuario: int

    nombre: str

    apellido: str

    correo: EmailStr

    telefono: str

    programa_formacion: str

    rol: str

    estado: bool

    fecha_registro: datetime

    class Config:
        from_attributes = True
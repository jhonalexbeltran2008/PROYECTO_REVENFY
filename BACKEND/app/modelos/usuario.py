from typing import Optional, List
from datetime import datetime

from sqlmodel import SQLModel, Field, Relationship


class Usuario(SQLModel, table=True):

    __tablename__ = "usuarios"

    id_usuario: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    nombre: str

    apellido: str

    correo: str = Field(
        index=True,
        unique=True
    )

    telefono: str

    programa_formacion: str

    rol: str = "Aprendiz"

    estado: bool = True

    fecha_registro: datetime = Field(
        default_factory=datetime.now
    )

    productos: List["Producto"] = Relationship(
        back_populates="usuario"
    )
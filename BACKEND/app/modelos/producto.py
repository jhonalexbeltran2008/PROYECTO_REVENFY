from typing import Optional

from sqlmodel import SQLModel, Field, Relationship


class Producto(SQLModel, table=True):

    __tablename__ = "productos"

    id_producto: Optional[int] = Field(
        default=None,
        primary_key=True
    )
    

    titulo: str

    descripcion: str

    categoria: str

    precio: float

    imagen: Optional[str] = None

    estado_producto: str = "Disponible"

    id_usuario: int = Field(
        foreign_key="usuarios.id_usuario"
    )

    usuario: Optional["Usuario"] = Relationship(
        back_populates="productos"
    )
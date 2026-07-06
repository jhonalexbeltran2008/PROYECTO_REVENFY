from pydantic import BaseModel


class ProductoCrear(BaseModel):

    titulo: str

    descripcion: str

    categoria: str

    precio: float

    imagen: str | None = None

    id_usuario: int


class ProductoActualizar(BaseModel):

    titulo: str | None = None

    descripcion: str | None = None

    categoria: str | None = None

    precio: float | None = None

    imagen: str | None = None

    estado_producto: str | None = None


class ProductoRespuesta(BaseModel):

    id_producto: int

    titulo: str

    descripcion: str

    categoria: str

    precio: float

    imagen: str | None

    estado_producto: str

    id_usuario: int

    class Config:
        from_attributes = True
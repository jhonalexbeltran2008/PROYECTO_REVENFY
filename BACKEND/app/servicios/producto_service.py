from sqlmodel import Session, select

from app.modelos.producto import Producto
from app.esquemas.producto import (
    ProductoCrear,
    ProductoActualizar
)


def listar_productos(sesion: Session):
    return sesion.exec(select(Producto)).all()


def obtener_producto(id_producto: int, sesion: Session):
    return sesion.get(Producto, id_producto)


def listar_productos_usuario(id_usuario: int, sesion: Session):

    consulta = select(Producto).where(
        Producto.id_usuario == id_usuario
    )

    return sesion.exec(consulta).all()


def crear_producto(datos: ProductoCrear, sesion: Session):

    producto = Producto.model_validate(datos)

    sesion.add(producto)
    sesion.commit()
    sesion.refresh(producto)

    return producto


def actualizar_producto(
    id_producto: int,
    datos: ProductoActualizar,
    sesion: Session
):

    producto = sesion.get(Producto, id_producto)

    if not producto:
        return None

    cambios = datos.model_dump(exclude_unset=True)

    for campo, valor in cambios.items():
        setattr(producto, campo, valor)

    sesion.add(producto)
    sesion.commit()
    sesion.refresh(producto)

    return producto


def eliminar_producto(
    id_producto: int,
    sesion: Session
):

    producto = sesion.get(Producto, id_producto)

    if not producto:
        return False

    sesion.delete(producto)
    sesion.commit()

    return True
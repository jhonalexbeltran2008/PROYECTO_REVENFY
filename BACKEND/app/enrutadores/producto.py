from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.conexion_bd import obtener_sesion

from app.esquemas.producto import (
    ProductoCrear,
    ProductoActualizar,
    ProductoRespuesta
)

from app.servicios.producto_service import (
    listar_productos,
    obtener_producto,
    listar_productos_usuario,
    crear_producto,
    actualizar_producto,
    eliminar_producto
)

router = APIRouter()

Sesion = Annotated[
    Session,
    Depends(obtener_sesion)
]


@router.get(
    "/",
    response_model=list[ProductoRespuesta]
)
def consultar_productos(
    sesion: Sesion
):

    return listar_productos(sesion)


@router.get(
    "/{id_producto}",
    response_model=ProductoRespuesta
)
def consultar_producto(
    id_producto: int,
    sesion: Sesion
):

    producto = obtener_producto(
        id_producto,
        sesion
    )

    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )

    return producto


@router.get(
    "/usuario/{id_usuario}",
    response_model=list[ProductoRespuesta]
)
def consultar_productos_usuario(
    id_usuario: int,
    sesion: Sesion
):

    return listar_productos_usuario(
        id_usuario,
        sesion
    )


@router.post(
    "/",
    response_model=ProductoRespuesta,
    status_code=status.HTTP_201_CREATED
)
def registrar_producto(
    datos: ProductoCrear,
    sesion: Sesion
):

    return crear_producto(
        datos,
        sesion
    )


@router.put(
    "/{id_producto}",
    response_model=ProductoRespuesta
)
def editar_producto(
    id_producto: int,
    datos: ProductoActualizar,
    sesion: Sesion
):

    producto = actualizar_producto(
        id_producto,
        datos,
        sesion
    )

    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )

    return producto


@router.delete("/{id_producto}")
def borrar_producto(
    id_producto: int,
    sesion: Sesion
):

    eliminado = eliminar_producto(
        id_producto,
        sesion
    )

    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )

    return {
        "mensaje": "Producto eliminado correctamente"
    }
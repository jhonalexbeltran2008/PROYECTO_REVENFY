from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.conexion_bd import obtener_sesion

from app.esquemas.usuario import (
    UsuarioCrear,
    UsuarioActualizar,
    UsuarioRespuesta
)

from app.servicios.usuario_service import (
    listar_usuarios,
    obtener_usuario,
    crear_usuario,
    actualizar_usuario,
    eliminar_usuario
)

router = APIRouter()

Sesion = Annotated[Session, Depends(obtener_sesion)]


@router.get("/", response_model=list[UsuarioRespuesta])
def consultar_usuarios(sesion: Sesion):
    return listar_usuarios(sesion)


@router.get("/{id_usuario}", response_model=UsuarioRespuesta)
def consultar_usuario(id_usuario: int, sesion: Sesion):

    usuario = obtener_usuario(id_usuario, sesion)

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    return usuario


@router.post(
    "/",
    response_model=UsuarioRespuesta,
    status_code=status.HTTP_201_CREATED
)
def registrar_usuario(datos: UsuarioCrear, sesion: Sesion):

    return crear_usuario(datos, sesion)


@router.put("/{id_usuario}", response_model=UsuarioRespuesta)
def editar_usuario(
    id_usuario: int,
    datos: UsuarioActualizar,
    sesion: Sesion
):

    usuario = actualizar_usuario(id_usuario, datos, sesion)

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    return usuario


@router.delete("/{id_usuario}")
def borrar_usuario(id_usuario: int, sesion: Sesion):

    eliminado = eliminar_usuario(id_usuario, sesion)

    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    return {
        "mensaje": "Usuario eliminado correctamente"
    }
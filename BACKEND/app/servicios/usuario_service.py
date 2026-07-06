from sqlmodel import Session, select

from app.modelos.usuario import Usuario
from app.esquemas.usuario import UsuarioCrear, UsuarioActualizar


def listar_usuarios(sesion: Session):
    return sesion.exec(select(Usuario)).all()


def obtener_usuario(id_usuario: int, sesion: Session):
    return sesion.get(Usuario, id_usuario)


def crear_usuario(datos: UsuarioCrear, sesion: Session):
    usuario = Usuario.model_validate(datos)

    sesion.add(usuario)
    sesion.commit()
    sesion.refresh(usuario)

    return usuario


def actualizar_usuario(id_usuario: int, datos: UsuarioActualizar, sesion: Session):

    usuario = sesion.get(Usuario, id_usuario)

    if not usuario:
        return None

    cambios = datos.model_dump(exclude_unset=True)

    for campo, valor in cambios.items():
        setattr(usuario, campo, valor)

    sesion.add(usuario)
    sesion.commit()
    sesion.refresh(usuario)

    return usuario


def eliminar_usuario(id_usuario: int, sesion: Session):

    usuario = sesion.get(Usuario, id_usuario)

    if not usuario:
        return False

    sesion.delete(usuario)
    sesion.commit()

    return True
from contextlib import asynccontextmanager
from sqlmodel import SQLModel, Session, create_engine
from .configuracion import configuracion

engine = create_engine(
    configuracion.DATABASE_URL,
    echo=True
)


def obtener_sesion():
    with Session(engine) as sesion:
        yield sesion


@asynccontextmanager
async def crear_tablas(app):
    SQLModel.metadata.create_all(engine)
    yield
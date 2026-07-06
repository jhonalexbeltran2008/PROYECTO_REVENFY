from fastapi import FastAPI

from .conexion_bd import crear_tablas
from .enrutadores.usuario import router as usuario_router
from .enrutadores.producto import router as producto_router

app = FastAPI(
    title="Revenfy API",
    version="1.0.0",
    lifespan=crear_tablas
)

app.include_router(
    usuario_router,
    prefix="/usuarios",
    tags=["Usuarios"]
)

app.include_router(
    producto_router,
    prefix="/productos",
    tags=["Productos"]
)


@app.get("/")
def inicio():
    return {
        "mensaje": "Bienvenido a Revenfy API"
    }
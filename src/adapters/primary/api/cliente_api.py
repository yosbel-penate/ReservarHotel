from fastapi import FastAPI, Depends, HTTPException
from typing import List
from .anotaciones.cliente import Cliente
from services.gestion_clientes import GestionClientes
from adapters.secondary.orm.sqlalchemy_cliente_repository import SQLAlchemyClienteRepository

app = FastAPI(
    title="API de Gestión de Clientes del Hotel",
    description="Esta es la API para gestionar clientes en el sistema de reservas del hotel.",
    version="1.0.0"
)

def get_gestion_clientes() -> GestionClientes:
    cliente_repository = SQLAlchemyClienteRepository(database_url="sqlite:///./test.db")
    return GestionClientes(cliente_repository)

@app.post("/clientes/", response_model=Cliente)
def crear_cliente(cliente: Cliente, gestion_clientes: GestionClientes = Depends(get_gestion_clientes)):
    gestion_clientes.crear_cliente(cliente)
    return cliente

@app.get("/clientes/{cliente_id}", response_model=Cliente)
def obtener_cliente(cliente_id: int, gestion_clientes: GestionClientes = Depends(get_gestion_clientes)):
    cliente = gestion_clientes.cliente_repository.obtener_cliente_por_id(cliente_id)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@app.get("/clientes/nombre/{nombre}", response_model=Cliente)
def obtener_cliente_por_nombre(nombre: str, gestion_clientes: GestionClientes = Depends(get_gestion_clientes)):
    cliente = gestion_clientes.cliente_repository.obtener_cliente_por_nombre(nombre)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

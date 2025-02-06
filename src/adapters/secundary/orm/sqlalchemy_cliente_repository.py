from typing import Optional

from src.domain.cliente import Cliente
from src.ports.cliente_repository import ClienteRepository

from .schemas.cliente_model import ClienteModel

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SQLAlchemyClienteRepository(ClienteRepository):
    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def obtener_cliente_por_id(self, id: int) -> Optional[Cliente]:
        session = self.Session()
        cliente_model = session.query(ClienteModel).filter_by(id=id).first()
        session.close()
        if cliente_model:
            return Cliente(id=cliente_model.id
                        , nombre=cliente_model.nombre
                        , informacion_contacto=cliente_model.informacion_contacto)
        return None

    def obtener_cliente_por_nombre(self, nombre: str) -> Optional[Cliente]:
        session = self.Session()
        cliente_model = session.query(ClienteModel).filter_by(nombre=nombre).first()
        session.close()
        if cliente_model:
            return Cliente(id=cliente_model.id
                        , nombre=cliente_model.nombre
                        , informacion_contacto=cliente_model.informacion_contacto)
        return None

    def guardar_cliente(self, cliente: Cliente):
        session = self.Session()
        cliente_model = ClienteModel(id=cliente.id
                                    , nombre=cliente.nombre
                                    , informacion_contacto=cliente.informacion_contacto)
        session.merge(cliente_model)
        session.commit()
        session.close()

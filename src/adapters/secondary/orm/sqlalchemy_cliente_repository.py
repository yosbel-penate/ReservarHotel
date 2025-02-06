from typing import Optional

from domain.cliente import Cliente
from .schemas.cliente_model import ClienteORM
from ports.cliente_repository import ClienteRepository

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


Base = declarative_base()

class SQLAlchemyClienteRepository(ClienteRepository):
    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        Base.metadata.create_all(bind=self.engine)

    def obtener_cliente_por_id(self, id: int) -> Optional[Cliente]:
        session = self.SessionLocal()
        try:
            cliente_model = session.query(ClienteORM).filter(ClienteORM.id == id).first()
            if cliente_model:
                return Cliente(id=cliente_model.id
                            , nombre=cliente_model.nombre
                            , informacion_contacto=cliente_model.informacion_contacto)
            return None
        finally:
            session.close()

    def obtener_cliente_por_nombre(self, nombre: str) -> Optional[Cliente]:
        session = self.SessionLocal()
        try:
            cliente_model = session.query(ClienteORM).filter(ClienteORM.nombre == nombre).first()
            if cliente_model:
                return Cliente(id=cliente_model.id
                            , nombre=cliente_model.nombre
                            , informacion_contacto=cliente_model.informacion_contacto)
            return None
        finally:
            session.close()

    def guardar_cliente(self, cliente: Cliente):
        session = self.SessionLocal()
        cliente_model = ClienteORM(id=cliente.id
                                    , nombre=cliente.nombre
                                    , informacion_contacto=cliente.informacion_contacto)
        session.merge(cliente_model)
        session.commit()
        session.close()

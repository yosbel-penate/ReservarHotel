from typing import Optional


class ClienteDatabaseAdapter(ClienteRepository):
    def __init__(self, db):
        self.db = db

    def obtener_cliente_por_id(self, id: int) -> Optional[Cliente]:
        # Implementación para obtener un cliente por ID
        pass

    def obtener_cliente_por_nombre(self, nombre: str) -> Optional[Cliente]:
        # Implementación para obtener un cliente por nombre
        pass

    def guardar_cliente(self, cliente: Cliente):
        # Implementación para guardar un cliente
        pass
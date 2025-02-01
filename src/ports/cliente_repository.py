from abc import ABC, abstractmethod
from typing import Optional

class ClienteRepository(ABC):
    @abstractmethod
    def obtener_cliente_por_id(self, id: int) -> Optional[Cliente]:
        pass

    @abstractmethod
    def obtener_cliente_por_nombre(self, nombre: str) -> Optional[Cliente]:
        pass

    @abstractmethod
    def guardar_cliente(self, cliente: Cliente):
        pass
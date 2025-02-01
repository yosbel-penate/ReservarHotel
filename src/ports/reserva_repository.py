from abc import ABC, abstractmethod
from typing import List, Optional
from ..domain.reserva import Reserva
from ..domain.cliente import Cliente

class ReservaRepository(ABC):
    @abstractmethod
    def obtener_reserva_por_id(self, id: int) -> Optional[Reserva]:
        pass

    @abstractmethod
    def obtener_reservas_por_cliente(self, cliente: Cliente) -> List[Reserva]:
        pass

    @abstractmethod
    def guardar_reserva(self, reserva: Reserva):
        pass
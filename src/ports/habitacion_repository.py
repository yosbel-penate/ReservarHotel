from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import date

class HabitacionRepository(ABC):
    @abstractmethod
    def obtener_habitacion_por_id(self, id: int) -> Optional[Habitacion]:
        pass

    @abstractmethod
    def obtener_habitaciones_disponibles(self, fecha_llegada: date, fecha_salida: date) -> List[Habitacion]:
        pass

    @abstractmethod
    def guardar_habitacion(self, habitacion: Habitacion):
        pass
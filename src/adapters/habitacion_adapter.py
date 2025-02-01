from typing import List, Optional
from datetime import date
from ..domain.habitacion import Habitacion
from ..ports.habitacion_repository import HabitacionRepository

class HabitacionDatabaseAdapter(HabitacionRepository):
    def __init__(self, db):
        self.db = db

    def obtener_habitacion_por_id(self, id: int) -> Optional[Habitacion]:
        # Implementación para obtener una habitación por ID
        pass

    def obtener_habitaciones_disponibles(self, fecha_llegada: date, fecha_salida: date) -> List[Habitacion]:
        # Implementación para obtener habitaciones disponibles
        pass

    def guardar_habitacion(self, habitacion: Habitacion):
        # Implementación para guardar una habitación
        pass
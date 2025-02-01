from ..domain.habitacion import Habitacion
from ..ports.habitacion_repository import HabitacionRepository

class GestionHabitaciones:
    def __init__(self, habitacion_repository: HabitacionRepository):
        self.habitacion_repository = habitacion_repository

    def crear_habitacion(self, habitacion: Habitacion):
        self.habitacion_repository.guardar_habitacion(habitacion)

    def modificar_habitacion(self, habitacion: Habitacion):
        self.habitacion_repository.guardar_habitacion(habitacion)

    def eliminar_habitacion(self, id: int):
        # Implementación para eliminar una habitación
        pass
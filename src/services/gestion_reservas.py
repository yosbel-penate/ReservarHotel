from typing import List
from datetime import date

class GestionReservas:
    def __init__(self, reserva_repository: ReservaRepository, habitacion_repository: HabitacionRepository, cliente_repository: ClienteRepository):
        self.reserva_repository = reserva_repository
        self.habitacion_repository = habitacion_repository
        self.cliente_repository = cliente_repository

    def crear_reserva(self, reserva: Reserva):
        self.reserva_repository.guardar_reserva(reserva)

    def cancelar_reserva(self, id: int):
        # Implementación para cancelar una reserva
        pass

    def buscar_habitaciones_disponibles(self, fecha_llegada: date, fecha_salida: date) -> List[Habitacion]:
        return self.habitacion_repository.obtener_habitaciones_disponibles(fecha_llegada, fecha_salida)

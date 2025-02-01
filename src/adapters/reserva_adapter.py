from typing import List, Optional


class ReservaDatabaseAdapter(ReservaRepository):
    def __init__(self, db):
        self.db = db

    def obtener_reserva_por_id(self, id: int) -> Optional[Reserva]:
        # Implementación para obtener una reserva por ID
        pass

    def obtener_reservas_por_cliente(self, cliente: Cliente) -> List[Reserva]:
        # Implementación para obtener reservas por cliente
        pass

    def guardar_reserva(self, reserva: Reserva):
        # Implementación para guardar una reserva
        pass
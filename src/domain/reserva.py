from datetime import date
from ..domain.cliente import Cliente
from ..domain.habitacion import Habitacion

class Reserva:
    def __init__(self, id: int, fecha_llegada: date, fecha_salida: date, cliente: Cliente, habitacion: Habitacion):
        self.id = id
        self.fecha_llegada = fecha_llegada
        self.fecha_salida = fecha_salida
        self.cliente = cliente
        self.habitacion = habitacion
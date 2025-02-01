from typing import List

class Habitacion:
    def __init__(self, id: int, numero: int, tipo: str, comodidades: List['Comodidad']):
        self.id = id
        self.numero = numero
        self.tipo = tipo
        self.comodidades = comodidades
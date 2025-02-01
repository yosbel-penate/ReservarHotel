from typing import List
from ..domain.comodidad import Comodidad

class Habitacion:
    def __init__(self, id: int, numero: int, tipo: str, comodidades: List[Comodidad]):
        self.id = id
        self.numero = numero
        self.tipo = tipo
        self.comodidades = comodidades
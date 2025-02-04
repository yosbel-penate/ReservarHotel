# Pasos para crear una nueva clase de dominio

1. **Crear la clase de dominio:**
   - Ubica el archivo en el directorio `src/domain/`.
   - Define la nueva clase `Reserva` con sus atributos y métodos necesarios.

2. **Actualizar el repositorio de la clase:**
   - Ubica el archivo en el directorio `src/ports/`.
   - Define una nueva interfaz `ReservaRepository` con los métodos necesarios para manejar las instancias de `Reserva`.

3. **Implementar los servicios:**
   - Ubica el archivo en el directorio `src/services/`.
   - Define una nueva clase `GestionReservas` que utilice `ReservaRepository` para manejar las operaciones de negocio relacionadas con `Reserva`.

4. **Escribir pruebas unitarias:**
   - Ubica el archivo en el directorio `test/`.
   - Escribe pruebas unitarias para la clase `Reserva`, `ReservaRepository` y `GestionReservas`.

## Ejemplo de implementación

### 1. Crear la clase de dominio

```python
# filepath: /d:/Projects/ReservarHotel/src/domain/reserva.py
class Reserva:
    def __init__(self, id: int, cliente_id: int, fecha_reserva: str, detalles: str):
        self.id = id
        self.cliente_id = cliente_id
        self.fecha_reserva = fecha_reserva
        self.detalles = detalles
```

### 2. Actualizar el repositorio de la clase

```python
# filepath: /d:/Projects/ReservarHotel/src/ports/reserva_repository.py
from abc import ABC, abstractmethod
from typing import Optional
from ..domain.reserva import Reserva

class ReservaRepository(ABC):
    @abstractmethod
    def obtener_reserva_por_id(self, id: int) -> Optional<Reserva]:
        pass

    @abstractmethod
    def guardar_reserva(self, reserva: Reserva):
        pass
```

### 3. Implementar los servicios

```python
# filepath: /d:/Projects/ReservarHotel/src/services/gestion_reservas.py
from ..domain.reserva import Reserva
from ..ports.reserva_repository import ReservaRepository

class GestionReservas:
    def __init__(self, reserva_repository: ReservaRepository):
        self.reserva_repository = reserva_repository

    def crear_reserva(self, reserva: Reserva):
        self.reserva_repository.guardar_reserva(reserva)

    def modificar_reserva(self, reserva: Reserva):
        self.reserva_repository.guardar_reserva(reserva)

    def eliminar_reserva(self, id: int):
        # Implementación para eliminar una reserva
        pass
```

### 4. Escribir pruebas unitarias

```python
# filepath: /d:/Projects/ReservarHotel/test/test_adapters.py
import unittest
from src.domain.reserva import Reserva
from src.services.gestion_reservas import GestionReservas
from src.ports.reserva_repository import ReservaRepository

class MockReservaRepository(ReservaRepository):
    def __init__(self):
        self.reservas = {}

    def obtener_reserva_por_id(self, id: int) -> Optional<Reserva]:
        return self.reservas.get(id)

    def guardar_reserva(self, reserva: Reserva):
        self.reservas[reserva.id] = reserva

class TestGestionReservas(unittest.TestCase):
    def setUp(self):
        self.repo = MockReservaRepository()
        self.gestion_reservas = GestionReservas(self.repo)

    def test_crear_reserva(self):
        reserva = Reserva(1, 1, "2023-10-01", "Detalles de la reserva")
        self.gestion_reservas.crear_reserva(reserva)
        self.assertEqual(self.repo.obtener_reserva_por_id(1), reserva)

    # ... otras pruebas ...

if __name__ == '__main__':
    unittest.main()

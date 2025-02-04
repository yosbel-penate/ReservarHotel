# Pasos para crear un nuevo adaptador API REST

1. **Definir las rutas de la API:**
   - Ubica el archivo en el directorio `src/adapters/api/`.
   - Define las rutas necesarias para manejar las operaciones de reservas (crear, modificar, eliminar, obtener).

2. **Implementar los controladores:**
   - Ubica el archivo en el directorio `src/adapters/api/controllers/`.
   - Define los controladores que manejarán las solicitudes HTTP y llamarán a los servicios correspondientes.

3. **Configurar el servidor:**
   - Ubica el archivo en el directorio `src/adapters/api/`.
   - Configura el servidor para que utilice las rutas y controladores definidos.

4. **Escribir pruebas de integración:**
   - Ubica el archivo en el directorio `test/integration/`.
   - Escribe pruebas de integración para las rutas de la API.

## Ejemplo de implementación

### 1. Definir las rutas de la API

```python
# filepath: /d:/Projects/ReservarHotel/src/adapters/api/routes.py
from flask import Flask
from .controllers.reserva_controller import ReservaController

app = Flask(__name__)

@app.route('/reservas', methods=['POST'])
def crear_reserva():
    return ReservaController.crear_reserva()

@app.route('/reservas/<int:id>', methods=['PUT'])
def modificar_reserva(id):
    return ReservaController.modificar_reserva(id)

@app.route('/reservas/<int:id>', methods=['DELETE'])
def eliminar_reserva(id):
    return ReservaController.eliminar_reserva(id)

@app.route('/reservas/<int:id>', methods=['GET'])
def obtener_reserva(id):
    return ReservaController.obtener_reserva(id)
```

### 2. Implementar los controladores

```python
# filepath: /d:/Projects/ReservarHotel/src/adapters/api/controllers/reserva_controller.py
from flask import request, jsonify
from ...services.gestion_reservas import GestionReservas
from ...domain.reserva import Reserva

class ReservaController:
    @staticmethod
    def crear_reserva():
        data = request.get_json()
        reserva = Reserva(**data)
        gestion_reservas.crear_reserva(reserva)
        return jsonify({"message": "Reserva creada"}), 201

    @staticmethod
    def modificar_reserva(id):
        data = request.get_json()
        reserva = Reserva(id, **data)
        gestion_reservas.modificar_reserva(reserva)
        return jsonify({"message": "Reserva modificada"}), 200

    @staticmethod
    def eliminar_reserva(id):
        gestion_reservas.eliminar_reserva(id)
        return jsonify({"message": "Reserva eliminada"}), 200

    @staticmethod
    def obtener_reserva(id):
        reserva = gestion_reservas.obtener_reserva_por_id(id)
        if reserva:
            return jsonify(reserva.__dict__), 200
        return jsonify({"message": "Reserva no encontrada"}), 404
```

### 3. Configurar el servidor

```python
# filepath: /d:/Projects/ReservarHotel/src/adapters/api/server.py
from .routes import app

if __name__ == '__main__':
    app.run(debug=True)
```

### 4. Escribir pruebas de integración

```python
# filepath: /d:/Projects/ReservarHotel/test/integration/test_api_reservas.py
import unittest
from src.adapters.api.server import app

class TestAPIReservas(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_crear_reserva(self):
        response = self.app.post('/reservas', json={
            "id": 1,
            "cliente_id": 1,
            "fecha_reserva": "2023-10-01",
            "detalles": "Detalles de la reserva"
        })
        self.assertEqual(response.status_code, 201)

    def test_obtener_reserva(self):
        response = self.app.get('/reservas/1')
        self.assertEqual(response.status_code, 200)

    # ... otras pruebas ...

if __name__ == '__main__':
    unittest.main()

# Pasos para crear un nuevo adaptador ORM SQLite

1. **Configurar la base de datos:**
   - Ubica el archivo en el directorio `src/adapters/orm/`.
   - Configura la conexión a la base de datos SQLite.

2. **Definir los modelos ORM:**
   - Ubica el archivo en el directorio `src/adapters/orm/models/`.
   - Define los modelos ORM correspondientes a las entidades del dominio.

3. **Implementar los repositorios:**
   - Ubica el archivo en el directorio `src/adapters/orm/repositories/`.
   - Implementa los repositorios que interactuarán con la base de datos a través de los modelos ORM.

4. **Escribir pruebas de integración:**
   - Ubica el archivo en el directorio `test/integration/`.
   - Escribe pruebas de integración para los repositorios ORM.

## Ejemplo de implementación

### 1. Configurar la base de datos

```python
# filepath: /d:/Projects/ReservarHotel/src/adapters/orm/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./reservar_hotel.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

### 2. Definir los modelos ORM

```python
# filepath: /d:/Projects/ReservarHotel/src/adapters/orm/models/reserva.py
from sqlalchemy import Column, Integer, String
from ..database import Base

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, index=True)
    fecha_reserva = Column(String, index=True)
    detalles = Column(String, index=True)
```

### 3. Implementar los repositorios

```python
# filepath: /d:/Projects/ReservarHotel/src/adapters/orm/repositories/reserva_repository.py
from sqlalchemy.orm import Session
from ...domain.reserva import Reserva as DomainReserva
from ..models.reserva import Reserva as ORMReserva

class ReservaRepository:
    def __init__(self, db: Session):
        self.db = db

    def obtener_reserva_por_id(self, id: int) -> DomainReserva:
        reserva = self.db.query(ORMReserva).filter(ORMReserva.id == id).first()
        if reserva:
            return DomainReserva(reserva.id, reserva.cliente_id, reserva.fecha_reserva, reserva.detalles)
        return None

    def guardar_reserva(self, reserva: DomainReserva):
        orm_reserva = ORMReserva(
            id=reserva.id,
            cliente_id=reserva.cliente_id,
            fecha_reserva=reserva.fecha_reserva,
            detalles=reserva.detalles
        )
        self.db.add(orm_reserva)
        self.db.commit()
        self.db.refresh(orm_reserva)
```

### 4. Escribir pruebas de integración

```python
# filepath: /d:/Projects/ReservarHotel/test/integration/test_orm_reserva_repository.py
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.adapters.orm.database import Base
from src.adapters.orm.models.reserva import Reserva as ORMReserva
from src.adapters.orm.repositories.reserva_repository import ReservaRepository
from src.domain.reserva import Reserva as DomainReserva

DATABASE_URL = "sqlite:///./test_reservar_hotel.db"

class TestORMReservaRepository(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine(DATABASE_URL)
        TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        Base.metadata.create_all(bind=self.engine)
        self.db = TestingSessionLocal()
        self.repo = ReservaRepository(self.db)

    def tearDown(self):
        Base.metadata.drop_all(bind=self.engine)
        self.db.close()

    def test_guardar_y_obtener_reserva(self):
        reserva = DomainReserva(1, 1, "2023-10-01", "Detalles de la reserva")
        self.repo.guardar_reserva(reserva)
        fetched_reserva = self.repo.obtener_reserva_por_id(1)
        self.assertEqual(fetched_reserva.id, reserva.id)
        self.assertEqual(fetched_reserva.cliente_id, reserva.cliente_id)
        self.assertEqual(fetched_reserva.fecha_reserva, reserva.fecha_reserva)
        self.assertEqual(fetched_reserva.detalles, reserva.detalles)

    # ... otras pruebas ...

if __name__ == '__main__':
    unittest.main()

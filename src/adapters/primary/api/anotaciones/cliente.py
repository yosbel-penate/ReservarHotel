from pydantic import BaseModel

class Cliente(BaseModel):
    id: int
    nombre: str
    informacion_contacto: str
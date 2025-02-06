from pydantic import BaseModel

class ClienteAnotacion(BaseModel):
    id: int
    nombre: str
    informacion_contacto: str
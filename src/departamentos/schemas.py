from pydantic import BaseModel, ConfigDict
from typing import List
from src.schemas.simples import ProfesorSimple

class DepartamentoBase(BaseModel):
    nombre: str

class DepartamentoCreate(DepartamentoBase):
    pass


class DepartamentoUpdate(BaseModel):
    nombre: str | None = None


class Departamento(DepartamentoBase):
    id: int
    profesores: List[ProfesorSimple]

    model_config = ConfigDict(from_attributes= True)

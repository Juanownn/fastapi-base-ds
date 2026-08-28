from pydantic import BaseModel, ConfigDict, EmailStr
from typing import List
from datetime import datetime
from src.schemas.simples import DepartamentoSimple

class ProfesorBase(BaseModel):
    nombre: str
    email: EmailStr
    departamento_id: int

class ProfesorCreate(ProfesorBase):
    pass


class ProfesorUpdate(ProfesorBase):
    nombre: str | None = None
    email: EmailStr | None = None
    departamento_id: int | None = None


class Profesor(ProfesorBase):
    id: int
    fecha_ingreso: datetime
    departamento: DepartamentoSimple
    #cursos: List[CursoSimple]

    model_config = ConfigDict(from_attributes= True)

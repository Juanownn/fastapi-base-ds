from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime


class DepartamentoSimple(BaseModel):
    id: int
    nombre: str

    model_config = ConfigDict(from_attributes=True)


class ProfesorSimple(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    departamento_id: int
    fecha_ingreso: datetime

    model_config = ConfigDict(from_attributes=True)


class ClaseSimple(BaseModel):
    id: int
    tema: str
    duracion_minutos: int
    curso_id: int

    model_config = ConfigDict(from_attributes=True)


class CursoSimple(BaseModel):
    id: int
    titulo: str
    creditos: int
    profesor_id: int

    model_config = ConfigDict(from_attributes=True)


class EstudianteSimple(BaseModel):
    id: int
    nombre: str
    legajo: int

    model_config = ConfigDict(from_attributes=True)


class InscripcionSimple(BaseModel):
    estudiante_id: int
    curso_id: int
    fecha_inscripcion: datetime
    calificacion_final: int

    model_config = ConfigDict(from_attributes=True)
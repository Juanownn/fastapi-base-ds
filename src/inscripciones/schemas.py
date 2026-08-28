from pydantic import BaseModel, ConfigDict
from datetime import datetime

from src.schemas.simples import EstudianteSimple, CursoSimple


class InscripcionBase(BaseModel):
    estudiante_id: int
    curso_id: int
    calificacion_final: int


class InscripcionCreate(InscripcionBase):
    pass


class InscripcionUpdate(BaseModel):
    calificacion_final: int | None = None


class Inscripcion(InscripcionBase):
    fecha_inscripcion: datetime
    estudiante: EstudianteSimple
    curso: CursoSimple

    model_config = ConfigDict(from_attributes=True)
from pydantic import BaseModel, ConfigDict

from src.schemas.simples import (
    ProfesorSimple,
    ClaseSimple,
    InscripcionSimple
)


class CursoBase(BaseModel):
    titulo: str
    creditos: int
    profesor_id: int


class CursoCreate(CursoBase):
    pass


class CursoUpdate(CursoBase):
    titulo: str | None = None
    creditos: int | None = None
    profesor_id: int | None = None


class Curso(CursoBase):
    id: int
    profesor: ProfesorSimple
    clases: list[ClaseSimple]
    inscripciones: list[InscripcionSimple]

    model_config = ConfigDict(from_attributes=True)
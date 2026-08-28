from pydantic import BaseModel, ConfigDict

from src.schemas.simples import InscripcionSimple


class EstudianteBase(BaseModel):
    nombre: str
    legajo: int


class EstudianteCreate(EstudianteBase):
    pass


class EstudianteUpdate(EstudianteBase):
    nombre: str | None = None
    legajo: int | None = None


class Estudiante(EstudianteBase):
    id: int
    inscripciones: list[InscripcionSimple]

    model_config = ConfigDict(from_attributes=True)
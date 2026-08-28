from pydantic import BaseModel, ConfigDict

from src.schemas.simples import CursoSimple


class ClaseBase(BaseModel):
    tema: str
    duracion_minutos: int
    curso_id: int


class ClaseCreate(ClaseBase):
    pass


class ClaseUpdate(ClaseBase):
    tema: str | None = None
    duracion_minutos: int | None = None
    curso_id: int | None = None


class Clase(ClaseBase):
    id: int
    curso: CursoSimple

    model_config = ConfigDict(from_attributes=True)
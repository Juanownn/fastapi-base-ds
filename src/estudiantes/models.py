from src.models import ModeloBase

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Estudiante(ModeloBase):
    __tablename__ = "estudiantes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    legajo: Mapped[int]

    inscripciones: Mapped[list["src.inscripciones.models.Inscripcion"]] = relationship(
        back_populates="estudiante"
    )
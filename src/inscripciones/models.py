from src.models import ModeloBase

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Inscripcion(ModeloBase):
    __tablename__ = "inscripciones"

    estudiante_id: Mapped[int] = mapped_column(
        ForeignKey("estudiantes.id"),
        primary_key=True
    )

    curso_id: Mapped[int] = mapped_column(
        ForeignKey("cursos.id"),
        primary_key=True
    )

    fecha_inscripcion: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )

    calificacion_final: Mapped[int]

    estudiante: Mapped["src.estudiantes.models.Estudiante"] = relationship(
        back_populates="inscripciones"
    )

    curso: Mapped["src.cursos.models.Curso"] = relationship(
        back_populates="inscripciones"
    )
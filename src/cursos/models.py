from src.models import ModeloBase

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Curso(ModeloBase):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))
    creditos: Mapped[int]

    profesor_id: Mapped[int] = mapped_column(ForeignKey("profesores.id"))

    profesor: Mapped["src.profesores.models.Profesor"] = relationship(
        back_populates="cursos"
    )

    clases: Mapped[list["src.clases.models.Clase"]] = relationship(
        back_populates="curso"
    )

    inscripciones: Mapped[list["src.inscripciones.models.Inscripcion"]] = relationship(
        back_populates="curso"
    )
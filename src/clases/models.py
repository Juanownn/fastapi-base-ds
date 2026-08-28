from src.models import ModeloBase

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Clase(ModeloBase):
    __tablename__ = "clases"

    id: Mapped[int] = mapped_column(primary_key=True)
    tema: Mapped[str] = mapped_column(String(100))
    duracion_minutos: Mapped[int]

    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))

    curso: Mapped["src.cursos.models.Curso"] = relationship(
        back_populates="clases"
    )
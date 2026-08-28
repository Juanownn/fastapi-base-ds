from src.models import ModeloBase
from datetime import datetime
from sqlalchemy import DateTime, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Profesor(ModeloBase):
    __tablename__ = "profesores"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(100), index=True)
    email: Mapped[str] = mapped_column(String(100))
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    #Clave foranea fisica de la DB
    departamento_id: Mapped[int] = mapped_column(ForeignKey("departamentos.id"))

    #Relacion ORM para navegacion con Departamento
    departamento: Mapped["src.departamentos.models.Departamento"] = relationship(back_populates="profesores")

    #Relacion con Cursos
    cursos: Mapped[list["src.cursos.models.Curso"]] = relationship(back_populates="profesor")
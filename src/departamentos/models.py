from src.models import ModeloBase
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Departamento(ModeloBase):
    __tablename__ = "departamentos"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(100))

    #Relacion ORM para navegacion con Profesores
    profesores: Mapped[list["src.profesores.models.Profesor"]] = relationship(back_populates="departamento")
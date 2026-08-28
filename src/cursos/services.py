import logging

from typing import List

from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session

from src.cursos.models import Curso
from src.schemas.simples import CursoSimple

from src.cursos import schemas
from src import exceptions


logger = logging.getLogger(__name__)


# operaciones CRUD para Curso
def crear_curso(db: Session, curso: schemas.CursoCreate) -> schemas.Curso:
    _curso = Curso(**curso.model_dump())

    db.add(_curso)
    db.commit()
    db.refresh(_curso)

    logger.info(f"Se creo un curso, con titulo {_curso.titulo}")

    return _curso


def listar_cursos(db: Session) -> List[schemas.Curso]:
    logger.info("Listando cursos desde services")

    return db.scalars(select(Curso)).all()


def leer_curso(curso_id: int, db: Session) -> schemas.Curso:
    db_curso = db.scalar(
        select(Curso).where(Curso.id == curso_id)
    )

    if db_curso is None:
        raise exceptions.NotFound

    return db_curso


def modificar_curso(
    db: Session,
    curso_id: int,
    curso: schemas.CursoUpdate
) -> Curso:

    db_curso = leer_curso(curso_id, db)

    db.execute(
        update(Curso)
        .where(Curso.id == curso_id)
        .values(**curso.model_dump(exclude_unset=True))
    )

    db.commit()
    db.refresh(db_curso)

    logger.info(
        f"Se actualizo correctamente el curso con id: "
        f"{db_curso.id} y titulo {db_curso.titulo}"
    )

    return db_curso


def eliminar_curso(db: Session, curso_id: int) -> CursoSimple:
    db_curso = leer_curso(curso_id, db)

    db.execute(
        delete(Curso).where(Curso.id == curso_id)
    )

    db.commit()

    return db_curso
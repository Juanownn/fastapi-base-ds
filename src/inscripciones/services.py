import logging

from typing import List

from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session

from src.inscripciones.models import Inscripcion
from src.schemas.simples import InscripcionSimple

from src.inscripciones import schemas
from src import exceptions


logger = logging.getLogger(__name__)


# operaciones CRUD para Inscripcion
def crear_inscripcion(
    db: Session,
    inscripcion: schemas.InscripcionCreate
) -> schemas.Inscripcion:

    _inscripcion = Inscripcion(**inscripcion.model_dump())

    db.add(_inscripcion)
    db.commit()
    db.refresh(_inscripcion)

    logger.info(
        f"Se creo una inscripcion para estudiante "
        f"{_inscripcion.estudiante_id} en curso {_inscripcion.curso_id}"
    )

    return _inscripcion


def listar_inscripciones(
    db: Session
) -> List[schemas.Inscripcion]:

    logger.info("Listando inscripciones desde services")

    return db.scalars(select(Inscripcion)).all()


def leer_inscripcion(
    estudiante_id: int,
    curso_id: int,
    db: Session
) -> schemas.Inscripcion:

    db_inscripcion = db.scalar(
        select(Inscripcion).where(
            Inscripcion.estudiante_id == estudiante_id,
            Inscripcion.curso_id == curso_id
        )
    )

    if db_inscripcion is None:
        raise exceptions.NotFound

    return db_inscripcion


def modificar_inscripcion(
    db: Session,
    estudiante_id: int,
    curso_id: int,
    inscripcion: schemas.InscripcionUpdate
) -> Inscripcion:

    db_inscripcion = leer_inscripcion(
        estudiante_id,
        curso_id,
        db
    )

    db.execute(
        update(Inscripcion)
        .where(
            Inscripcion.estudiante_id == estudiante_id,
            Inscripcion.curso_id == curso_id
        )
        .values(**inscripcion.model_dump(exclude_unset=True))
    )

    db.commit()
    db.refresh(db_inscripcion)

    logger.info(
        f"Se actualizo correctamente la inscripcion del estudiante "
        f"{db_inscripcion.estudiante_id} en el curso "
        f"{db_inscripcion.curso_id}"
    )

    return db_inscripcion


def eliminar_inscripcion(
    db: Session,
    estudiante_id: int,
    curso_id: int
) -> InscripcionSimple:

    db_inscripcion = leer_inscripcion(
        estudiante_id,
        curso_id,
        db
    )

    db.execute(
        delete(Inscripcion).where(
            Inscripcion.estudiante_id == estudiante_id,
            Inscripcion.curso_id == curso_id
        )
    )

    db.commit()

    return db_inscripcion
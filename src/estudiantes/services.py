import logging

from typing import List

from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session

from src.estudiantes.models import Estudiante
from src.schemas.simples import EstudianteSimple

from src.estudiantes import schemas
from src import exceptions


logger = logging.getLogger(__name__)


# operaciones CRUD para Estudiante
def crear_estudiante(
    db: Session,
    estudiante: schemas.EstudianteCreate
) -> schemas.Estudiante:

    _estudiante = Estudiante(**estudiante.model_dump())

    db.add(_estudiante)
    db.commit()
    db.refresh(_estudiante)

    logger.info(
        f"Se creo un estudiante, con nombre {_estudiante.nombre}"
    )

    return _estudiante


def listar_estudiantes(db: Session) -> List[schemas.Estudiante]:
    logger.info("Listando estudiantes desde services")

    return db.scalars(select(Estudiante)).all()


def leer_estudiante(
    estudiante_id: int,
    db: Session
) -> schemas.Estudiante:

    db_estudiante = db.scalar(
        select(Estudiante).where(Estudiante.id == estudiante_id)
    )

    if db_estudiante is None:
        raise exceptions.NotFound

    return db_estudiante


def modificar_estudiante(
    db: Session,
    estudiante_id: int,
    estudiante: schemas.EstudianteUpdate
) -> Estudiante:

    db_estudiante = leer_estudiante(estudiante_id, db)

    db.execute(
        update(Estudiante)
        .where(Estudiante.id == estudiante_id)
        .values(**estudiante.model_dump(exclude_unset=True))
    )

    db.commit()
    db.refresh(db_estudiante)

    logger.info(
        f"Se actualizo correctamente el estudiante con id: "
        f"{db_estudiante.id} y nombre {db_estudiante.nombre}"
    )

    return db_estudiante


def eliminar_estudiante(
    db: Session,
    estudiante_id: int
) -> EstudianteSimple:

    db_estudiante = leer_estudiante(estudiante_id, db)

    db.execute(
        delete(Estudiante).where(Estudiante.id == estudiante_id)
    )

    db.commit()

    return db_estudiante
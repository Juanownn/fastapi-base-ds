import logging
from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.profesores.models import Profesor
from src.schemas.simples import ProfesorSimple
from src.profesores import schemas
from src import exceptions

# Creamos un logger para este módulo específico. Más info.:
# https://docs.python.org/3/library/logging.html

logger = logging.getLogger(__name__)


# operaciones CRUD para Profesor

def crear_profesor(db: Session, profesor: schemas.ProfesorCreate) -> schemas.Profesor:
    _profesor = Profesor(**profesor.model_dump())
    db.add(_profesor)
    db.commit()
    db.refresh(_profesor)
    logger.info(f"Se creo un profesor, con nombre {_profesor.nombre}")
    return _profesor


def listar_profesores(db: Session) -> List[schemas.Profesor]:
    logger.info("Listando profesores desde services")
    return db.scalars(select(Profesor)).all()


def leer_profesor(profesor_id: int, db: Session) -> schemas.Profesor:
    db_profesor = db.scalar(select(Profesor).where(Profesor.id == profesor_id))
    if db_profesor is None:
        raise exceptions.NotFound
    return db_profesor


def modificar_profesor(
        db: Session, profesor_id: int, profesor: schemas.ProfesorUpdate
) -> Profesor:
    db_profesor = leer_profesor(profesor_id, db)
    db.execute(
        update(Profesor)
        .where(Profesor.id == profesor_id)
        .values(**profesor.model_dump(exclude_unset=True))
    )
    db.commit()
    db.refresh(db_profesor)
    logger.info(
        f"Se actualizo correctamente el profesor con id: "
        f"{db_profesor.id} y nombre {db_profesor.nombre}"
    )
    return db_profesor


def eliminar_profesor(db: Session, profesor_id: int) -> ProfesorSimple:
    db_profesor = leer_profesor(profesor_id, db)
    db.execute(
        delete(Profesor).where(Profesor.id == profesor_id)
    )
    db.commit()
    return db_profesor


import logging
from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.profesores.models import Profesor
from src.profesores import schemas
from src import exceptions

# Creamos un logger para este módulo específico. Más info.: https://docs.python.org/3/library/logging.html
logger = logging.getLogger(__name__)

# operaciones CRUD para Personas

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

def leer_profesor(db:Session, profesor_id: int) -> schemas.Profesor:
    db_profesor = db.scalar(select(Profesor).where(Profesor.id == profesor_id))
    if db_profesor is None:
        raise exceptions.NotFound
    return(db_profesor)

def modificar_profesor(
        db: Session, profesor_id: int, profesor: schemas.ProfesorUpdate
) -> Profesor:
    db_profesor = leer_profesor(db, profesor_id)
    db.execute(
        update(Profesor).where(Profesor.id == profesor_id).values(**profesor.model_dump())
    )
    db.commit()
    db.refresh(db_profesor)
    logger.info(f"Se actualizo correctamente el profesor con id: {db_profesor.id} y nombre {db_profesor.nombre}")
    return db_profesor

def eliminar_profesor(db:Session, profesor_id: int) -> schemas.Profesor:
    db_profesor = leer_profesor(db, profesor_id)
    db.execute(delete(Profesor).where(Profesor.id == profesor_id))
    db.commit()
    return db_profesor


def eliminar_persona(db: Session, persona_id: int) -> schemas.Persona:
    db_persona = leer_persona(db, persona_id)
    if len(db_persona.mascotas) > 0:
        raise exceptions.PersonaTieneMascotas()
    db.execute(delete(Persona).where(Persona.id == persona_id))
    db.commit()
    return db_persona

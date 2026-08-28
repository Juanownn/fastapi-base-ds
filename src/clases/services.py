import logging

from typing import List

from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session

from src.clases.models import Clase
from src.schemas.simples import ClaseSimple

from src.clases import schemas
from src import exceptions


logger = logging.getLogger(__name__)


# operaciones CRUD para Clase
def crear_clase(db: Session, clase: schemas.ClaseCreate) -> schemas.Clase:
    _clase = Clase(**clase.model_dump())

    db.add(_clase)
    db.commit()
    db.refresh(_clase)

    logger.info(f"Se creo una clase, con tema {_clase.tema}")

    return _clase


def listar_clases(db: Session) -> List[schemas.Clase]:
    logger.info("Listando clases desde services")

    return db.scalars(select(Clase)).all()


def leer_clase(clase_id: int, db: Session) -> schemas.Clase:
    db_clase = db.scalar(
        select(Clase).where(Clase.id == clase_id)
    )

    if db_clase is None:
        raise exceptions.NotFound

    return db_clase


def modificar_clase(
    db: Session,
    clase_id: int,
    clase: schemas.ClaseUpdate
) -> Clase:

    db_clase = leer_clase(clase_id, db)

    db.execute(
        update(Clase)
        .where(Clase.id == clase_id)
        .values(**clase.model_dump(exclude_unset=True))
    )

    db.commit()
    db.refresh(db_clase)

    logger.info(
        f"Se actualizo correctamente la clase con id: "
        f"{db_clase.id} y tema {db_clase.tema}"
    )

    return db_clase


def eliminar_clase(db: Session, clase_id: int) -> ClaseSimple:
    db_clase = leer_clase(clase_id, db)

    db.execute(
        delete(Clase).where(Clase.id == clase_id)
    )

    db.commit()

    return db_clase
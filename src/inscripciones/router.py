import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.inscripciones import schemas, services
from src.schemas.simples import InscripcionSimple


logger = logging.getLogger(__name__)


router = APIRouter(
    prefix="/inscripcion",
    tags=["inscripciones"]
)


# Rutas para inscripcion
@router.post("/", response_model=schemas.Inscripcion)
def create_inscripcion(
    inscripcion: schemas.InscripcionCreate,
    db: Session = Depends(get_db)
):
    return services.crear_inscripcion(db, inscripcion)


@router.get("/", response_model=list[schemas.Inscripcion])
def read_inscripciones(
    db: Session = Depends(get_db)
):
    logger.info(
        "Consultando la lista de inscripciones desde endpoint..."
    )

    return services.listar_inscripciones(db)


@router.get(
    "/{estudiante_id}/{curso_id}",
    response_model=schemas.Inscripcion
)
def read_inscripcion(
    estudiante_id: int,
    curso_id: int,
    db: Session = Depends(get_db)
):
    return services.leer_inscripcion(
        estudiante_id,
        curso_id,
        db
    )


@router.put(
    "/{estudiante_id}/{curso_id}",
    response_model=schemas.Inscripcion
)
def update_inscripcion(
    estudiante_id: int,
    curso_id: int,
    inscripcion: schemas.InscripcionUpdate,
    db: Session = Depends(get_db)
):
    return services.modificar_inscripcion(
        db,
        estudiante_id,
        curso_id,
        inscripcion
    )


@router.delete(
    "/{estudiante_id}/{curso_id}",
    response_model=InscripcionSimple
)
def delete_inscripcion(
    estudiante_id: int,
    curso_id: int,
    db: Session = Depends(get_db)
):
    return services.eliminar_inscripcion(
        db,
        estudiante_id,
        curso_id
    )
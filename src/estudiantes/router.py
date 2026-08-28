import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.estudiantes import schemas, services
from src.schemas.simples import EstudianteSimple


logger = logging.getLogger(__name__)


router = APIRouter(
    prefix="/estudiante",
    tags=["estudiantes"]
)


# Rutas para estudiante
@router.post("/", response_model=schemas.Estudiante)
def create_estudiante(
    estudiante: schemas.EstudianteCreate,
    db: Session = Depends(get_db)
):
    return services.crear_estudiante(db, estudiante)


@router.get("/", response_model=list[schemas.Estudiante])
def read_estudiantes(
    db: Session = Depends(get_db)
):
    logger.info(
        "Consultando la lista de estudiantes desde endpoint..."
    )

    return services.listar_estudiantes(db)


@router.get("/{estudiante_id}", response_model=schemas.Estudiante)
def read_estudiante(
    estudiante_id: int,
    db: Session = Depends(get_db)
):
    return services.leer_estudiante(estudiante_id, db)


@router.put("/{estudiante_id}", response_model=schemas.Estudiante)
def update_estudiante(
    estudiante_id: int,
    estudiante: schemas.EstudianteUpdate,
    db: Session = Depends(get_db)
):
    return services.modificar_estudiante(
        db,
        estudiante_id,
        estudiante
    )


@router.delete(
    "/{estudiante_id}",
    response_model=EstudianteSimple
)
def delete_estudiante(
    estudiante_id: int,
    db: Session = Depends(get_db)
):
    return services.eliminar_estudiante(db, estudiante_id)
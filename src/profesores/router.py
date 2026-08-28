import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.profesores import schemas, services
from src.schemas.simples import ProfesorSimple

# Creamos un logger para este módulo específico. Más info.:
# https://docs.python.org/3/library/logging.html

logger = logging.getLogger(__name__)
router = APIRouter(
    prefix="/profesor",
    tags=["profesores"]
)

# Rutas para profesor

@router.post("/", response_model=schemas.Profesor)
def create_profesor(
    profesor: schemas.ProfesorCreate,
    db: Session = Depends(get_db)
):
    return services.crear_profesor(db, profesor)

@router.get("/", response_model=list[schemas.Profesor])
def read_profesores(db: Session = Depends(get_db)):
    logger.info("Consultando la lista de profesores desde endpoint...")
    return services.listar_profesores(db)


@router.get("/{profesor_id}", response_model=schemas.Profesor)
def read_profesor(profesor_id: int, db: Session = Depends(get_db)):
    return services.leer_profesor(profesor_id, db)


@router.put("/{profesor_id}", response_model=schemas.Profesor)
def update_profesor(
    profesor_id: int,
    profesor: schemas.ProfesorUpdate,
    db: Session = Depends(get_db)
):
    return services.modificar_profesor(db, profesor_id, profesor)


@router.delete("/{profesor_id}", response_model=ProfesorSimple)
def delete_profesor(profesor_id: int, db: Session = Depends(get_db)):
    return services.eliminar_profesor(db, profesor_id)
import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.clases import schemas, services
from src.schemas.simples import ClaseSimple


logger = logging.getLogger(__name__)


router = APIRouter(
    prefix="/clase",
    tags=["clases"]
)


# Rutas para clase
@router.post("/", response_model=schemas.Clase)
def create_clase(
    clase: schemas.ClaseCreate,
    db: Session = Depends(get_db)
):
    return services.crear_clase(db, clase)


@router.get("/", response_model=list[schemas.Clase])
def read_clases(db: Session = Depends(get_db)):
    logger.info("Consultando la lista de clases desde endpoint...")

    return services.listar_clases(db)


@router.get("/{clase_id}", response_model=schemas.Clase)
def read_clase(
    clase_id: int,
    db: Session = Depends(get_db)
):
    return services.leer_clase(clase_id, db)


@router.put("/{clase_id}", response_model=schemas.Clase)
def update_clase(
    clase_id: int,
    clase: schemas.ClaseUpdate,
    db: Session = Depends(get_db)
):
    return services.modificar_clase(db, clase_id, clase)


@router.delete("/{clase_id}", response_model=ClaseSimple)
def delete_clase(
    clase_id: int,
    db: Session = Depends(get_db)
):
    return services.eliminar_clase(db, clase_id)
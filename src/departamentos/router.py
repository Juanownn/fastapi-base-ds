import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.departamentos import schemas, services
from src.schemas.simples import DepartamentoSimple

# Creamos un logger para este módulo específico. Más info.: https://docs.python.org/3/library/logging.html
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/departamento", tags=["departamentos"])

# Rutas para departamento

@router.post("/", response_model=schemas.Departamento)
def create_departamento(departamento: schemas.DepartamentoCreate, db: Session = Depends(get_db)):
    return services.crear_departamento(db, departamento)

@router.get("/", response_model=list[schemas.Departamento])
def read_departamentos(db: Session = Depends(get_db)):
    logger.info("Consultando la lista de departamentos desde endpoint...")
    return services.listar_departamentos(db)

@router.get("/{departamento.id}", response_model=schemas.Departamento)
def read_departamento(departamento_id: int, db: Session = Depends(get_db)):
    return services.leer_departamento(db, departamento_id)

@router.put("/{departamento.id}", response_model=schemas.Departamento)
def update_departamento(departamento_id: int, departamento: schemas.DepartamentoUpdate, db: Session = Depends(get_db)):
    return services.modificar_departamento(db, departamento_id, departamento)

@router.delete("/{departamento.id}", response_model=DepartamentoSimple)
def delete_departamento(departamento_id: int, db: Session = Depends(get_db)):
    return services.eliminar_departamento(db, departamento_id)

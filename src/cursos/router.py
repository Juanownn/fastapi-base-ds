import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.cursos import schemas, services
from src.schemas.simples import CursoSimple


logger = logging.getLogger(__name__)


router = APIRouter(
    prefix="/curso",
    tags=["cursos"]
)


# Rutas para curso
@router.post("/", response_model=schemas.Curso)
def create_curso(
    curso: schemas.CursoCreate,
    db: Session = Depends(get_db)
):
    return services.crear_curso(db, curso)


@router.get("/", response_model=list[schemas.Curso])
def read_cursos(db: Session = Depends(get_db)):
    logger.info("Consultando la lista de cursos desde endpoint...")

    return services.listar_cursos(db)


@router.get("/{curso_id}", response_model=schemas.Curso)
def read_curso(
    curso_id: int,
    db: Session = Depends(get_db)
):
    return services.leer_curso(curso_id, db)


@router.put("/{curso_id}", response_model=schemas.Curso)
def update_curso(
    curso_id: int,
    curso: schemas.CursoUpdate,
    db: Session = Depends(get_db)
):
    return services.modificar_curso(db, curso_id, curso)


@router.delete("/{curso_id}", response_model=CursoSimple)
def delete_curso(
    curso_id: int,
    db: Session = Depends(get_db)
):
    return services.eliminar_curso(db, curso_id)
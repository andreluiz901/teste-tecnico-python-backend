from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.focus_log import FocusLog
from app.schemas.focus_log import (
    FocusLogCreate,
    FocusLogResponse
)

from app.services.diagnostic_service import (
    generate_productivity_diagnostic
)

router = APIRouter()


@router.get("/")
def health():
    return {"status": "ok"}


@router.post(
    "/registro-foco",
    response_model=FocusLogResponse
)
def create_focus_log(
    data: FocusLogCreate,
    db: Session = Depends(get_db)
):
    focus_log = FocusLog(
        nivel_foco=data.nivel_foco,
        tempo_minutos=data.tempo_minutos,
        comentario=data.comentario,
        categoria=data.categoria,
        interrupcoes=data.interrupcoes
    )

    db.add(focus_log)

    db.commit()

    db.refresh(focus_log)

    return focus_log

@router.get(
    "/registros-foco",
    response_model=list[FocusLogResponse]
)
def list_focus_logs(
    db: Session = Depends(get_db)
):
    focus_logs = db.query(FocusLog).all()

    return focus_logs

@router.get("/diagnostico-produtividade")
def get_productivity_diagnostic(
    db: Session = Depends(get_db)
):
    focus_logs = db.query(FocusLog).all()

    diagnostic = generate_productivity_diagnostic(
        focus_logs
    )

    return diagnostic
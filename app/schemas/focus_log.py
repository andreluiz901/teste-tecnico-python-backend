from pydantic import BaseModel
from pydantic import Field


class FocusLogCreate(BaseModel):
    nivel_foco: int = Field(..., ge=1, le=5)

    tempo_minutos: int = Field(..., gt=0)

    comentario: str = Field(
        ...,
        min_length=3,
        max_length=300
    )

    categoria: str = Field(
        ...,
        min_length=3,
        max_length=50
    )

    interrupcoes: int = Field(
        ...,
        ge=0,
        le=50
    )


class FocusLogResponse(FocusLogCreate):
    id: int

    class Config:
        from_attributes = True
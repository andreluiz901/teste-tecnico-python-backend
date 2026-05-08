from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.core.database import Base


class FocusLog(Base):
    __tablename__ = "focus_logs"

    id = Column(Integer, primary_key=True, index=True)

    nivel_foco = Column(Integer)

    tempo_minutos = Column(Integer)

    comentario = Column(String)

    categoria = Column(String)

    interrupcoes = Column(Integer)
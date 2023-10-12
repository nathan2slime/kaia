from schemas.base import BaseModel, Mapped, mapped_column, Base
from sqlalchemy.orm import relationship
from typing import List
from schemas.answer import Answer
import enum

class QuestionType(enum.Enum):
    MATH = "MATH"
    PORTUGUESE = "PORTUGUESE"
    SCIENSE = "SCIENSE"
    HISTORY = "HISTORY"
    NONE = "NONE"

class Question(BaseModel, Base):
    __tablename__ = "questions"

    title: Mapped[str] = mapped_column()
    type: Mapped[QuestionType] = mapped_column(default=QuestionType.NONE)
    thumb: Mapped[str | None] = mapped_column()
    answers: Mapped[List[Answer.__name__]] = relationship()
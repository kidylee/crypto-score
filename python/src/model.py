import uuid as uuid_pkg

from sqlmodel import SQLModel, Field


def auto_uuid() -> str:
    return str(uuid_pkg.uuid4())


class ReputationScore(SQLModel, table=True):
    __tablename__ = "reputation_score"
    address: str = Field(default_factory=auto_uuid, nullable=False, primary_key=True)
    wallet_type: str 
    score: int

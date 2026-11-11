"""Model tabel database."""
from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text

from database.session import Base


def _now() -> datetime:
    return datetime.now(timezone.utc)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    subscription_tier = Column(String(20), default="free", nullable=False)  # free, creator, pro
    created_at = Column(DateTime(timezone=True), default=_now, nullable=False)


class GenerationLog(Base):
    __tablename__ = "generation_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # kosong = pengguna tamu
    prompt = Column(Text, nullable=False)
    result = Column(Text, nullable=True)
    model = Column(String(100), nullable=True)
    status = Column(String(20), default="success", nullable=False)  # success, error
    created_at = Column(DateTime(timezone=True), default=_now, nullable=False)

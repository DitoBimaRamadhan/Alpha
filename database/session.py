"""Koneksi database (SQLite secara default, PostgreSQL lewat DATABASE_URL)."""
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

DEFAULT_DATABASE_URL = f"sqlite:///{ROOT_DIR / 'alpha.db'}"
DATABASE_URL = os.getenv("DATABASE_URL") or DEFAULT_DATABASE_URL

# SQLite butuh opsi khusus agar bisa dipakai dari beberapa thread (FastAPI).
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


def init_db() -> None:
    """Membuat semua tabel jika belum ada."""
    from database import models  # noqa: F401  (mendaftarkan model ke Base)

    Base.metadata.create_all(bind=engine)


def get_db():
    """Dependency FastAPI: membuka sesi database per request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

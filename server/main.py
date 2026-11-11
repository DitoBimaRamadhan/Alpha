"""Titik masuk aplikasi: API + file frontend dalam satu server.

Jalankan dari root proyek:
    uvicorn server.main:app --reload
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from database import init_db
from server.config import ROOT_DIR, get_settings
from server.routes import health, text

FRONTEND_DIR = ROOT_DIR / "frontend"


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()  # buat tabel database saat server start
    yield


settings = get_settings()
app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API
app.include_router(health.router)
app.include_router(text.router)

# Frontend (HTML, CSS, JS) disajikan dari folder frontend/
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")

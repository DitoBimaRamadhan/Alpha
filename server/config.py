"""Konfigurasi server, dibaca dari environment / file .env di root proyek."""
from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ROOT_DIR / ".env", extra="ignore")

    APP_NAME: str = "ALPHA AI"
    GROQ_API_KEY: str = ""
    GROQ_MODEL: str = "openai/gpt-oss-20b"
    SYSTEM_PROMPT: str = "You are ALPHA AI, a premium content generator."
    # Daftar origin yang boleh memanggil API, dipisah koma. "*" = semua.
    CORS_ORIGINS: str = "*"

    @property
    def cors_origins(self) -> list[str]:
        return [o.strip() for o in self.CORS_ORIGINS.split(",") if o.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()

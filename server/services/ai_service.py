"""Layanan pemanggilan model AI di Groq."""
from groq import APIError, APIStatusError, AsyncGroq

from server.config import get_settings


class AIServiceError(Exception):
    """Error yang pesannya aman ditampilkan ke pengguna."""

    def __init__(self, message: str, status_code: int = 502):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


_client: AsyncGroq | None = None


def _get_client() -> AsyncGroq:
    global _client
    settings = get_settings()
    if not settings.GROQ_API_KEY:
        raise AIServiceError(
            "GROQ_API_KEY belum diatur. Tambahkan ke file .env lalu jalankan ulang server.",
            status_code=503,
        )
    if _client is None:
        _client = AsyncGroq(api_key=settings.GROQ_API_KEY)
    return _client


async def generate_text(prompt: str) -> str:
    settings = get_settings()
    client = _get_client()
    try:
        completion = await client.chat.completions.create(
            model=settings.GROQ_MODEL,
            messages=[
                {"role": "system", "content": settings.SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
        )
    except APIStatusError as exc:
        detail = exc.message
        if isinstance(exc.body, dict):
            detail = (exc.body.get("error") or {}).get("message", detail)
        raise AIServiceError(f"Groq menolak permintaan ({exc.status_code}): {detail}") from exc
    except APIError as exc:
        raise AIServiceError(f"Gagal menghubungi Groq: {exc.message}") from exc
    return (completion.choices[0].message.content or "").strip()

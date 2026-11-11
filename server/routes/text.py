"""Endpoint API untuk generate teks."""
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from database import get_db
from database.models import GenerationLog
from server.config import get_settings
from server.services import ai_service

router = APIRouter(prefix="/api/text", tags=["text"])


class TextRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=4000)


class TextResponse(BaseModel):
    result: str


@router.post("/generate", response_model=TextResponse)
async def generate_text(request: TextRequest, db: Session = Depends(get_db)):
    prompt = request.prompt.strip()
    if not prompt:
        return JSONResponse(status_code=400, content={"detail": "Prompt tidak boleh kosong."})

    model = get_settings().GROQ_MODEL
    try:
        result = await ai_service.generate_text(prompt)
    except ai_service.AIServiceError as exc:
        db.add(GenerationLog(prompt=prompt, result=exc.message, model=model, status="error"))
        db.commit()
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})

    db.add(GenerationLog(prompt=prompt, result=result, model=model, status="success"))
    db.commit()
    return TextResponse(result=result)

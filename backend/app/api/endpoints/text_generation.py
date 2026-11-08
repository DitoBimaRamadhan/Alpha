from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.ai_service import AIService

router = APIRouter()

class TextRequest(BaseModel):
    prompt: str

class TextResponse(BaseModel):
    result: str

@router.post("/generate", response_model=TextResponse)
async def generate_text(request: TextRequest):
    if not request.prompt:
        raise HTTPException(status_code=400, detail="Prompt empty")

    result = await AIService.generate_text(request.prompt)
    return TextResponse(result=result)

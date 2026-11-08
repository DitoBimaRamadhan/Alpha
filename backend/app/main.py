from fastapi import FastAPI
from app.api.endpoints import text_generation

app = FastAPI(title="ALPHA AI")

app.include_router(text_generation.router, prefix="/api/text", tags=["text"])

@app.get("/")
def read_root():
    return {"status": "ALPHA AI Active"}

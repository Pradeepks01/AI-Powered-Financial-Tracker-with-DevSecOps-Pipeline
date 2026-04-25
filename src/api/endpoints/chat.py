from fastapi import APIRouter, Depends, HTTPException
import httpx
from src.core.config import settings
from src.schemas import chat as chat_schemas
from src.api.endpoints.auth import get_current_user
from src.db import models

router = APIRouter()

@router.post("/", response_model=chat_schemas.ChatResponse)
async def chat_with_ai(
    request: chat_schemas.ChatRequest,
    current_user: models.User = Depends(get_current_user)
):
    # Simple logic to talk to Ollama
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{settings.OLLAMA_URL}/api/generate",
                json={
                    "model": "tinyllama",
                    "prompt": f"You are a financial advisor. User says: {request.message}. Give a short, helpful financial advice.",
                    "stream": False
                },
                timeout=30.0
            )
            if response.status_code == 200:
                reply = response.json().get("response", "I'm not sure how to respond to that.")
                return {"reply": reply}
            else:
                return {"reply": "AI Advisor is currently unavailable. Please try again later."}
    except Exception as e:
        return {"reply": "Failed to connect to AI Advisor. Ensure Ollama is running."}

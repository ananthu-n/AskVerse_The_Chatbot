from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from backend.chatbot import get_bot_response
from fastapi_jwt_auth import AuthJWT

router = APIRouter()

class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    response: str

@router.post("/chat", response_model=ChatResponse)
async def chat_with_bot(request: ChatRequest, Authorize: AuthJWT = Depends()):
    # Require user authentication
    Authorize.jwt_required()

    prompt = request.prompt.strip()
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt is required.")

    try:
        response = await get_bot_response(prompt)  # ← Always await
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating bot response: {str(e)}")

    return {"response": response}

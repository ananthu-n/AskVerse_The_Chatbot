from pydantic import BaseModel, EmailStr, Field

# -------------------- USER SCHEMAS --------------------

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

# -------------------- TOKEN SCHEMAS --------------------

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

# -------------------- CHAT SCHEMAS --------------------

class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    response: str

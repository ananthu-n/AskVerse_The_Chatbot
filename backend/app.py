import os
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

# CORS setup - allow all for dev; restrict in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Settings(BaseModel):
    authjwt_secret_key: str = os.getenv("JWT_SECRET_KEY", "secret_key_should_be_set_in_env")

@AuthJWT.load_config
def get_config():
    return Settings()

class User(BaseModel):
    username: str
    password: str

users_db = {}

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})

@app.get("/")
def read_root():
    return {"message": "FastAPI server is running!"}

@app.post('/register')
def register(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.username] = user.password
    return {"msg": "User registered successfully"}

@app.post('/login')
def login(user: User, Authorize: AuthJWT = Depends()):
    if users_db.get(user.username) != user.password:
        raise HTTPException(status_code=401, detail="Bad username or password")
    access_token = Authorize.create_access_token(subject=user.username)
    return {"access_token": access_token}

from backend.database import init_db
init_db()

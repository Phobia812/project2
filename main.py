from fastapi import FastAPI
from models import User
from routers import router as users_router

app = FastAPI()

app.include_router(users_router)

from fastapi import FastAPI
from database import init_db
from routers import router as users_router

app = FastAPI()

init_db()

app.include_router(users_router)

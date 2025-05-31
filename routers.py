from fastapi import APIRouter, HTTPException
from models import User, UserCreate
from data import users

router = APIRouter()

@router.get("/users", response_model=list[User])
def get_users():
    return users

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Користувача не знайдено")

@router.post("/create_user", response_model=User)
def create_user(user_data: UserCreate):
    for existing_user in users:
        if existing_user.email == user_data.email:
            raise HTTPException(status_code=400, detail="Користувач з таким email вже існує")
    
    new_id = max(u.id for u in users) + 1 if users else 1
    new_user = User(id=new_id, username=user_data.username, email=user_data.email)
    users.append(new_user)
    return new_user
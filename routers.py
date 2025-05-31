from fastapi import APIRouter, HTTPException
from schemas import User, UserCreate
import crud

router = APIRouter()

@router.get("/users/", response_model=list[User])
def get_users():
    users = crud.get_all_users()
    if not users:
        raise HTTPException(status_code=404, detail="Користувачів не знайдено")
    return users

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = crud.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Користувача не знайдено")
    return user

@router.post("/create_user/", response_model=User)
def create_new_user(user: UserCreate):
    existing_user = crud.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Користувач з таким email вже існує")
    
    existing_username = crud.get_user_by_username(user.username)
    if existing_username:
        raise HTTPException(status_code=400, detail="Користувач з таким username вже існує")
    
    return crud.create_user(user)
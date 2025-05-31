from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    username: str
    email: EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
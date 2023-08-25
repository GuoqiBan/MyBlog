from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    code: Optional[int] = False
    message: str = None
    result: Optional[dict] = None

class LoginModel(BaseModel):
    username: str = None
    password: str = None

class CreateModel(UserBase):
    password: str


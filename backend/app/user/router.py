import os
from datetime import timedelta
from sqlalchemy.orm import Session
from app.common.database import SessionLocal, engine, get_db
from fastapi import FastAPI, HTTPException, Form, Depends, status, APIRouter
from app.user.schemas import UserBase, LoginModel
from app.user.crud import check_user, create_access_token, check_jwt_token, ACCESS_TOKEN_EXPIRE_MINUTES
from starlette.responses import FileResponse

router = APIRouter(prefix="/user", tags=["user"])

# 登录接口api
@router.post("/login")
async def login_for_access_token(loginmodel: LoginModel, db: Session = Depends(get_db)):
    user = check_user(loginmodel.username, loginmodel.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误"
        )
    # 过期时间
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # 把id进行username加密，要使用str类型
    access_token = create_access_token(
        data={"sub": user}, expires_delta=access_token_expires
    )
    return {"code": 0, "message": "登录成功", "result": {"token": access_token, "id": 1}}

# 访问当前用户信息接口api
@router.get("/getUserInfoById")
async def get_user(id: int, token:str):
    print(id)
    return {"code": 0, "result": {"nick_name": "Ban", "id": 1, "avatar":f"http://localhost:8080/api/photo/get_avatar?id=3"}}
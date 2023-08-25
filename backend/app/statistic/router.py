import os
from datetime import timedelta
from sqlalchemy.orm import Session
from app.common.database import SessionLocal, engine, get_db
from fastapi import FastAPI, HTTPException, Form, Depends, status, APIRouter
from app.statistic.crud import get_statistic_by_db

router = APIRouter(prefix="/statistic", tags=["statistic"])

# 条件分页获取文章
@router.get("")
async def get_statistic(db: Session = Depends(get_db)):
    result = get_statistic_by_db(db)
    if result:
        message = {"code":0, "result": result}
    else:
        message = {"code":-1}
    return message

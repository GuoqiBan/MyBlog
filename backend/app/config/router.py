import os
from datetime import timedelta
from sqlalchemy.orm import Session
from app.common.database import SessionLocal, engine, get_db
from fastapi import FastAPI, HTTPException, Form, Depends, status, APIRouter
from app.config.crud import  get_blog_config, add_blog_times

router = APIRouter(prefix="/config", tags=["config"])

@router.get("")
async def get_config(db: Session = Depends(get_db)):
    get_result = get_blog_config(db)
    if get_result:
        result = {
            "code": 0,
            "result": get_result
        }
    else:
        result = {
            "code": -1
        }
    return result

@router.put("/addView")
async def addView(db: Session = Depends(get_db)):
    get_result = add_blog_times(db)
    if get_result:
        result = {
            "code": 0,
            "result": get_result
        }
    else:
        result = {
            "code": -1
        }
    return result

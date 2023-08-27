import os
from datetime import timedelta
from sqlalchemy.orm import Session
from app.common.database import SessionLocal, engine, get_db
from fastapi import FastAPI, HTTPException, Form, Depends, status, APIRouter
from app.tag.crud import  get_tags

router = APIRouter(prefix="/tag", tags=["tag"])

@router.get("/getTagDictionary")
async def get_tag(db: Session = Depends(get_db)):
    get_result = get_tags(db)
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

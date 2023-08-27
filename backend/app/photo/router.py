import os
from datetime import timedelta
from sqlalchemy.orm import Session
from app.common.database import SessionLocal, engine, get_db
from fastapi import FastAPI, HTTPException, Form, Depends, status, APIRouter
from app.photo.crud import  get_avatar_by_id, get_bg_by_id

router = APIRouter(prefix="/photo", tags=["photo"])

@router.get("/get_avatar")
async def get_avatar(id: int=3):
    get_result = get_avatar_by_id(id)
    if get_result:
        return get_result

@router.get("/get_bg")
async def get_bg(id: int=3):
    get_result = get_bg_by_id(id)
    if get_result:
        return get_result
import datetime
from jose import jwt
import logging
from typing import Optional
from fastapi import Header, status, HTTPException
from passlib.context import CryptContext
from pydantic import ValidationError
from app.common.models import BlogConfig
from sqlalchemy.orm import Session
from starlette.responses import FileResponse

def get_avatar_by_id(id):
    filename = f"./file_service/avatar_{id}.jpg"
    return FileResponse(filename)

def get_bg_by_id(id):
    filename = f"./file_service/bg_{id}.jpg"
    return FileResponse(filename)
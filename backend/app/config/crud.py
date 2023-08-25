import datetime
from jose import jwt
import logging
from typing import Optional
from fastapi import Header, status, HTTPException
from passlib.context import CryptContext
from pydantic import ValidationError
from app.common.models import BlogConfig
from sqlalchemy.orm import Session

def get_blog_config(db: Session):
    get_query = db.query(BlogConfig).first()
    return get_query

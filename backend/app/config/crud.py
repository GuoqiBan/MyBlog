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

def add_blog_times(db: Session):
    get_query = db.query(BlogConfig).first()
    print(get_query.view_time)
    if get_query.view_time is None:
        get_view_time = 0
    else:
        get_view_time = get_query.view_time + 1
    get_query.view_time = get_view_time
    db.commit()
    db.close()
    return True

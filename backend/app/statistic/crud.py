import datetime
from jose import jwt
import logging
from typing import Optional
from fastapi import Header, status, HTTPException
from passlib.context import CryptContext
from pydantic import ValidationError
from app.common.models import BlogArticle
from sqlalchemy.orm import Session

def get_statistic_by_db(db: Session):
    get_Article = db.query(BlogArticle).all()
    statistic_dict = {
        "articleCount": len(get_Article)
    }
    return statistic_dict
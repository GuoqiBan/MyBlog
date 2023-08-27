import datetime
from jose import jwt
import logging
from typing import Optional
from fastapi import Header, status, HTTPException
from passlib.context import CryptContext
from pydantic import ValidationError
from app.common.models import BlogArticle, BlogTag, BlogCategory
from sqlalchemy.orm import Session

def get_statistic_by_db(db: Session):
    get_Article = db.query(BlogArticle).all()
    get_tag = db.query(BlogTag).all()
    get_categroy = db.query(BlogCategory).all()
    statistic_dict = {
        "articleCount": len(get_Article),
        "tagCount": len(get_tag),
        "categoryCount": len(get_categroy)
    }
    return statistic_dict
import datetime
from jose import jwt
import logging
from typing import Optional
from fastapi import Header, status, HTTPException
from passlib.context import CryptContext
from pydantic import ValidationError
from app.common.models import BlogArticle
from sqlalchemy.orm import Session

def get_article_by_page(start_page, end_page, db: Session):
    get_query = db.query(BlogArticle).all()
    return get_query

def create_article():
    pass

def get_article_by_id(article_id, db: Session):
    get_query = db.query(BlogArticle).filter(BlogArticle.id == article_id).first()
    return get_query
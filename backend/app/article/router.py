import os
from datetime import timedelta
from sqlalchemy.orm import Session
from app.common.database import SessionLocal, engine, get_db
from fastapi import FastAPI, HTTPException, Form, Depends, status, APIRouter
from app.article.crud import create_article, get_article_by_page

router = APIRouter(prefix="/article", tags=["article"])

# 条件分页获取文章
@router.get("/blogHomeGetArticleList")
async def get_article(current: int, size: int, db: Session = Depends(get_db)):
    result = get_article_by_page(current, size, db)
    if result:
        message = {"code":0, "result": {"list": result, "total": len(result)}}
    else:
        message = {"code":-1}
    return message

# 新增文章
@router.post("/createArticle")
async def create_article(tagList: list,):
    result = create_article()
    return
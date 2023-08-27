import os
from datetime import timedelta
from sqlalchemy.orm import Session
from app.common.database import SessionLocal, engine, get_db
from fastapi import FastAPI, HTTPException, Form, Depends, status, APIRouter
from app.article.crud import create_article, get_article_by_page, get_article_by_id

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

@router.get("/getArticleById")
async def getArticleById(article_id: int, db: Session = Depends(get_db)):
    get_result = get_article_by_id(article_id, db)
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

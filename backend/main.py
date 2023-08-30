import uvicorn
from fastapi import FastAPI
from app.user import router as user_router
from app.article import router as article_router
from app.config import router as config_router
from app.statistic import router as statistic_router
from app.photo import router as photo_router
from app.tag import router as tag_router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(title="Blog")

app.include_router(user_router.router)
app.include_router(article_router.router)
app.include_router(config_router.router)
app.include_router(statistic_router.router)
app.include_router(tag_router.router)
app.include_router(photo_router.router)

app.add_middleware(
    CORSMiddleware,
    # 允许跨域的源列表，例如 ["http://www.example.org"] 等等，["*"] 表示允许任何源
    allow_origins="http://ban.ates.top",
    # 跨域请求是否支持 cookie，默认是 False，如果为 True，allow_origins 必须为具体的源，不可以是 ["*"]
    allow_credentials=True,
    # 允许跨域请求的 HTTP 方法列表，默认是 ["GET"]
    allow_methods=["*"],
    # 允许跨域请求的 HTTP 请求头列表，默认是 []，可以使用 ["*"] 表示允许所有的请求头
    # 当然 Accept、Accept-Language、Content-Language 以及 Content-Type 总之被允许的
    allow_headers=["*"],
    # 可以被浏览器访问的响应头, 默认是 []，一般很少指定
    # expose_headers=["*"]
    # 设定浏览器缓存 CORS 响应的最长时间，单位是秒。默认为 600，一般也很少指定
    # max_age=1000
)

if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8081, reload=True)

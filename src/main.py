from fastapi import FastAPI

from blogs.blog import blog_router
from users.user import user_router

from data_access.database import init_db


def build_app() -> FastAPI:
    app = FastAPI (
        title="Blog app",
        description="This is simple blog app"
    )

    app.include_router(blog_router, prefix='/blogs')
    app.include_router(user_router, prefix='/user')


    return app

app = build_app()
celery = app.celery_app

@app.on_event("startup")
async def connect():
    await init_db()

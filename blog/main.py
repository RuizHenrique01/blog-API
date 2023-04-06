from fastapi import FastAPI
import uvicorn
from . import models
from .database import engine
from .router import user, blog, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router=user.router)
app.include_router(router=blog.router)
app.include_router(router=auth.router)



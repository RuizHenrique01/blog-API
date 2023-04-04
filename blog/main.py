from fastapi import FastAPI
from . import models
from .database import engine
from .router import user, blog

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router=user.router)
app.include_router(router=blog.router)


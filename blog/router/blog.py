from fastapi import APIRouter, Depends, status
from typing import Annotated
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import blog
from ..repository.oauth2 import get_current_user

router = APIRouter(
    tags=['Blogs'],
    prefix='/blog'
)

get_db = get_db

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog,
           current_user: Annotated[schemas.TokenData, Depends(get_current_user)], db: Session = Depends(get_db),):
    return blog.create(schemas.CreateBlog(
        title=request.title,
        body=request.body,
        user_id=current_user.username
    ), db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    return blog.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)

@router.get('/', status_code=status.HTTP_200_OK, response_model=list[schemas.ShowBlog])
def get_all(db: Session = Depends(get_db)):
    return blog.get_all(db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_one(id: int, db: Session = Depends(get_db)):
    return blog.get_one(id, db)
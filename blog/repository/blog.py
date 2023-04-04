from fastapi import status, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} not found.")
    
    blog.delete(synchronize_session=False)
    db.commit()
    return {'message': 'Success delete'}

def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} not found.")
    
    blog.update(request.dict())
    db.commit()
    return { 'message': 'updated' }

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def get_one(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog {id} not found!')
    
    return blog
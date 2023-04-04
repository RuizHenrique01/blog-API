from fastapi import status, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session
from ..hashing import Hash

def create(request: schemas.User, db: Session):
    user_exist = db.query(models.User).filter(models.User.email == request.email).first()

    if user_exist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='This user already exists.')
    
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_one(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User {id} not found!')
    
    return user
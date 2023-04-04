from fastapi import APIRouter, Depends, status
from .. import schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

get_db = get_db

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_one_user(id: int, db: Session = Depends(get_db)):
    return user.get_one(id, db)
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from typing import Annotated
from ..repository import auth
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix='/auth',
    tags=['Authentication']
)

get_db = get_db

@router.post('/login', status_code=status.HTTP_200_OK)
def login(request: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    return auth.login(request, db)

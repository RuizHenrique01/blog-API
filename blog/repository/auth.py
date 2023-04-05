from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models
from ..hashing import Hash
from . import token

def login(request: schemas.Login, db: Session):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid login.')

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid login.')

    token_generated = token.create_access_token(data={"sub": user.email})

    return {"access_token": token_generated, "token_type": "bearer"}

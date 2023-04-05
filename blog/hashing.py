from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:
    def bcrypt(password: str):
        return pwd_context.hash(password)

    def verify(password_hashed: str, password_plain: str):
        return pwd_context.verify(password_plain, password_hashed)
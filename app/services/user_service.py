from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.database.models import User
from app.schemas.user import UserCreate
from app.core.security import hash_password, verify_password


class UserService:

    @staticmethod
    def create_user(user_data: UserCreate, db: Session) -> User:
        # Verifica se email já existe
        exists = db.query(User).filter(User.email == user_data.email).first()
        if exists:
            raise HTTPException(status_code=400, detail="Email already registered")

        new_user = User(
            email=user_data.email,
            hashed_password=hash_password(user_data.password)
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    @staticmethod
    def authenticate(email: str, password: str, db: Session) -> User:
        user = db.query(User).filter(User.email == email).first()

        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        return user

    @staticmethod
    def get_user_by_email(email: str, db: Session) -> User | None:
        return db.query(User).filter(User.email == email).first()

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.user import UserCreate
from app.core.security import create_access_token
from app.services.user_service import UserService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = UserService.create_user(user, db)
    return {"message": "User created successfully", "user_id": new_user.id}


@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    authenticated_user = UserService.authenticate(
        user.email, user.password, db)

    token = create_access_token({"sub": authenticated_user.email})

    return {"access_token": token, "token_type": "bearer"}

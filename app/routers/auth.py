from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.database.models import User
from app.core.security import create_access_token, verify_password
from app.schemas.user import UserCreate
from app.core.security import hash_password

router = APIRouter(prefix="/auth", tags=["auth"])  # Rota para autenticação

# Rota para registrar um novo usuário


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    # Verifica se o usuário já existe
    exists = db.query(User).filter(User.email == user.email).first()

    # Verifica se o email já está em uso
    if exists:
        raise HTTPException(status_code=400, detail="Email já está em uso.")

    # Cria um novo usuário
    new_user = User(
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    # Adiciona o novo usuário ao banco de dados
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "Usuário registrado com sucesso."}

# Rota para login de usuário


@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    # Busca o usuário pelo email
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas.")

    token = create_access_token(
        {"sub": db_user.email})  # Gera o token de acesso

    # Retorna o token de acesso
    return {"access_token": token, "token_type": "bearer"}

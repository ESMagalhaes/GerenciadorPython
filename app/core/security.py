# Importando os módulos necessários
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from app.core.config import settings

# Contexto de criptografia
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    """Função para gerar o hash de uma senha"""
    return pwd_context.hash(password)

def verify_password(simple_pswd: str, hashed_pswd: str):
    """Função para verificar se a senha simples corresponde ao hash"""
    return pwd_context.verify(simple_pswd, hashed_pswd)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
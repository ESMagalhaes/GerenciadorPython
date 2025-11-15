# Importando os módulos necessários
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseModel):  # Classe de configuração usando Pydantic
    secret_key: str = os.getenv("SECRET_KEY")
    algorithm: str = os.getenv("ALGORITHM")
    access_token_expire_minutes: int = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

    db_url: str = os.getenv("DATABASE_URL")


settings = Settings()  # Instância das configurações

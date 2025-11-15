# Importando os módulos necessários
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

db_url = os.getenv("DATABASE_URL")

# Configuração da conexão com o banco de dados
engine = create_engine(
    db_url,
    pool_pre_ping=True
)

# Criação da classe base para os modelos
Base = declarative_base()
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Função para obter uma sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

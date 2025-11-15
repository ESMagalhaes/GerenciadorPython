# Importando os módulos necessários
from fastapi import FastAPI
from app.routers import auth, users, tasks
from app.database.connection import Base, engine
from pydantic import BaseModel, EmailStr

# Modelo Pydantic para criação de usuário
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Modelo Pydantic para resposta de usuário
class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True
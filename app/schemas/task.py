from pydantic import BaseModel

# Modelo Pydantic base para tarefa
class TaskBase(BaseModel):
    title: str
    description: str | None = None

# Modelo Pydantic para criação de tarefa
class TaskCreate(TaskBase):
    pass

# Modelo Pydantic para resposta de tarefa
class TaskResponse(TaskBase):
    id: int
    completed: bool

    class Config:
        from_attributes = True

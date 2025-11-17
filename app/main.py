from fastapi import FastAPI
from app.routers import auth, users, tasks

app = FastAPI(title="Task Manager API")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "API is running!"}

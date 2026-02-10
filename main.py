from fastapi import FastAPI
from routers import todos
from database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(todos.router)

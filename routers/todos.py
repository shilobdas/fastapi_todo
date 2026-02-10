from fastapi import APIRouter, Depends, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import get_db
from crud import create_todo, get_all_todos, delete_todo
from schemas import TodoCreate
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Index page: Show table
@router.get("/")
def read_todos(request: Request, db: Session = Depends(get_db)):
    todos = get_all_todos(db)
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

# Create page: Show form
@router.get("/create")
def create_page(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

# Handle form submission
@router.post("/create")
def create_todo_form(
    title: str = Form(...),
    description: str = Form(""),
    completed: bool = Form(False),
    db: Session = Depends(get_db)
):
    todo = TodoCreate(title=title, description=description, completed=completed)
    create_todo(db, todo)
    return RedirectResponse("/", status_code=303)

# Delete todo
@router.post("/todos/{todo_id}/delete")
def delete(todo_id: int, db: Session = Depends(get_db)):
    
    delete_todo(db, todo_id)
    return RedirectResponse("/", status_code=303)

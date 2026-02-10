from sqlalchemy.orm import Session
from models import ToDo
from schemas import TodoCreate

def get_all_todos(db: Session):
    return db.query(ToDo).all()

def create_todo(db: Session, todo: TodoCreate):
    db_todo = ToDo(
        title=todo.title,
        description=todo.description,
        completed=todo.completed
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()

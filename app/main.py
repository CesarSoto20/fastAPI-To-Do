from fastapi import FastAPI, Depends
from app.models import Todo
from app.database import SessionLocal, engine
from app import database_models 
from sqlalchemy.orm import Session 



app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)


todos = [
    Todo(id=1, title="Monday", description="clean the room", completed=True),
    Todo(id=2, title="Tuesday", description="mop the house", completed=False),
    Todo(id=8, title="Sunday", description="go to the gym", completed=True),
    Todo(id=4, title="Friday", description="Go for a 20min run", completed=False)
]
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = SessionLocal()

    count =  db.query(database_models.Todo).count()

    if count == 0:
        for todo in todos:
            db.add(database_models.Todo(**todo.model_dump()))
        db.commit()

init_db()

@app.get("/")
def greet():
    return "Hello to the user"

@app.get("/todos")
def get_all_todos(db: Session = Depends (get_db)):
    db_todos = db.query(database_models.Todo).all()
    return db_todos

@app.get("/todo/{id}")
def get_todo_by_id(id: int, db: Session = Depends(get_db)):
    db_todo = db.query(database_models.Todo).filter(database_models.Todo.id == id).first()
    if db_todo:
        return db_todo 
    return "Todo list not found!"



@app.post("/todo")
def add_todo(todo: Todo, db: Session = Depends(get_db)):
    db.add(database_models.Todo(**todo.model_dump()))
    db.commit()
    return todo



@app.put("/todo")
def update_todo (id:int, todo:Todo, db: Session = Depends(get_db)):
    db_todo = db.query(database_models.Todo).filter(database_models.Todo.id == id).first()
    if db_todo:
        db_todo.title = todo.title
        db_todo.description = todo.description
        db_todo.completed = todo.completed
        db.commit()
        return "todo has been updated"
    else:
        return "Todo not Found!"


@app.delete("/todo")
def delete_todo(id:int, db: Session = Depends(get_db)):
    db_todo = db.query(database_models.Todo).filter(database_models.Todo.id == id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
        return "Todo has been deleted"
    else:
        return "Todo not found"


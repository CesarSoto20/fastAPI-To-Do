from fastapi import FastAPI
from app.models import Todo


app = FastAPI()


todos = [
    Todo(id=1, title="Monday", description="clean the room", completed=True),
    Todo(id=2, title="Tuesday", description="mop the house", completed=False),
    Todo(id=8, title="Sunday", description="go to the gym", completed=True),
    Todo(id=4, title="Friday", description="Go for a 20min run", completed=False)
]
    
@app.get("/")
def greet():
    return "Hello to the user"

@app.get("/todos")
def get_all_todos():
    return todos

@app.get("/todo/{id}")
def get_todo_by_id(id: int):
    for todo in todos:
        if todo.id == id:
            return todo 
    return "Todo list not found!"



@app.post("/todo")
def add_todo(todo: Todo):
    todos.append(todo)
    return todo



@app.put("/todo")
def update_todo (id:int, todo:Todo):
    for i in range(len(todos)):
        if todos[i].id == id:
            todos[i] = todo
            return "Todo has been changed."
    return "Todo not Found!"



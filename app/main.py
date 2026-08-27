from fastapi import FastAPI
from app.models import todo
app = FastAPI()

todos = [
    todo(id=1, title="Monday", description="clean the room", completed=True),
    todo(id=3, title="Tuesday", description="mop the house", completed=False),
    todo(id=4, title="Sunday", description="go to the gym", completed=True),
    todo(id=7, title="Friday", description="Go for a 20min run", completed=False)
]
    

@app.get("/")
def greet():
    return "Hello to the user"

@app.get("/todos")
def get_all_todos():
    return todos
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Request Body model
class Todo(BaseModel):
    id: int
    task: str
    status: str

# In-memory database
todos: List[Todo] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the To-Do API"}

@app.get("/todo")
def get_todos():
    return todos

@app.post("/todo")
def add_todo(todo: Todo):
    todos.append(todo)
    return {"message": "To-do added successfully"}

@app.put("/todo/{id}")
def update_todo(id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == id:
            todos[index] = updated_todo
            return {"message": "To-do updated successfully"}
    return {"error": "To-do not found"}

@app.delete("/todo/{id}")
def delete_todo(id: int):
    for todo in todos:
        if todo.id == id:
            todos.remove(todo)
            return {"message": "To-do deleted successfully"}
    return {"error": "To-do not found"}
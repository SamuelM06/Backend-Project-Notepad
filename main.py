from typing import Union

from fastapi import FastAPI
from models import User, Notes


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/{user_id}")
def read_user(user_id: int, q: Union[str, None] = None):
    return {"user_id": user_id, "q": q}


@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {"user_name": user.name, "user_id": user_id}

@app.put("/notes/{note_id}")
def update_note(note_id: int, note: Notes):
    return {"title": note.title, "user_id": note.user_id, "note_id": note_id}


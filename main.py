from fastapi import FastAPI
from models import User, Notes
app = FastAPI()

app.title = "Backend-Project-Notepad"

#Home 
@app.get("/", tags=["Root"])
def root():
    return {"Mensaje:": "Bienvenido a Backend-Project-Notepad"}

#User
#register_user
@app.get("/user",tags=["User"])
def create_user(user: User):
    return {""}

#delete_user
@app.delete("/user/{user_id}",tags=["User"])
def delete_user(user_id: int, user: User):
    return {""}



#Notes

app.get("/notes", tags=["Notes"])
def search_notes(note:Notes):
    return{""}

app.get("/notes/{IdN}", tags=["Notes"])
def search_notes_id(note_id):
    return{"mesaage": f"Nota {note_id}"}

@app.post("/notes", tags=["Notes"])
def create_note(note: Notes):
    return {"message": "Nota creada", "data": note}

@app.put("/notes/{note_id}",tags=["Notes"])
def update_note(note_id: int, note: Notes):
    return {"message": f"Nota {note_id} actualizada", "data": note}

@app.delete("/notes/{note_id}", tags=["Notes"])
def delete_note(note_id: int):
    return {"message": f"Nota {note_id} eliminada"}


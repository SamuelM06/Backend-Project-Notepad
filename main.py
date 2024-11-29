from typing import Union
from fastapi import FastAPI
from models import User, Notes
from database import create_db_and_tables, SessionDep
from fastapi import HTTPException


create_db_and_tables()

app = FastAPI()

app.title = "Backend-Project-Notepad"

# Root
@app.get("/", tags=["Root"])
def root():
    return {"Mensaje:": "Bienvenido a Backend-Project-Notepad"}

# User
@app.post("/user", tags=["User"])
def create_user(user: User, session: SessionDep):
    session.add(user)
    session.commit()
    session.refresh(user)
    return {"message" : "Usuario creado exitosamente","data": user ,}
    

@app.delete("/user/{user_id}", tags=["User"])
def delete_user(user_id:int, session: SessionDep): 
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"Usuario eliminado": True}


#Probando metodos primero en usuario


# Notes: Crear nota
@app.post("/notes", tags=["Notes"])
def create_note(note: Notes):  
    return {"message": "Nota creada exitosamente"}

# Notes: Buscar todas las notas
@app.get("/notes", tags=["Notes"])
def search_notes(): 
    return {"message": "Notas encontradas"}

# Notes: Buscar nota por ID
@app.get("/notes/{note_id}", tags=["Notes"])
def search_notes_id(note_id: int):  # Usa get_db aquí
    return {"message": "Nota encontrada"}

# Notes: Actualizar nota
@app.put("/notes/{note_id}", tags=["Notes"])
def update_note(note_id: int):
    return {"message": f"Nota {note_id} actualizada"}

# Notes: Eliminar nota
@app.delete("/notes/{note_id}", tags=["Notes"])
def delete_note(note_id: int):
    return {"message": f"Nota {note_id} eliminada"}

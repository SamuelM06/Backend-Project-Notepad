from typing import Union,Annotated
from fastapi import FastAPI
from models import User, Notes
from database import create_db_and_tables, SessionDep
from fastapi import HTTPException,Query
from datetime import datetime
from sqlalchemy import select


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


#Metodos en usuario listos



#Inicio prueba metodos Notes

# Notes: Crear nota
@app.post("/notes", tags=["Notes"])
def create_note(note: Notes, session:SessionDep):  
    note.date = datetime.strptime(note.date, '%Y-%m-%d').date()
    session.add(note)
    session.commit()
    session.refresh(note)
    return {"message" : "Nota creada exitosamente","data": note}


# Notes: Buscar todas las notas
@app.get("/notes", tags=["Notes"])
def search_notes(session: SessionDep): 
    try:
        notes = session.exec(select(Notes)).all()
        all_notes = [note[0].dict() for note in notes]
        return all_notes
    except Exception as e: 
        return {"error": str(e)}  


# Notes: Buscar nota por ID
@app.get("/notes/{note_id}", tags=["Notes"])
def search_notes_id(note_id: int, session:SessionDep): 
    note = session.get(Notes, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"Nota encontrada":note}


# Notes: Editar nota
@app.put("/notes/{note_id}", tags=["Notes"])
def update_note(note_id: int, session:SessionDep, note_data: Notes):
    note_db=session.get(Notes, note_id)
    if not note_db:
         raise HTTPException(status_code=404, detail="Nota no encontrada")
    if note_data.title is not None:
        note_db.title = note_data.title
    if note_data.description is not None:
        note_db.description = note_data.description
        session.add(note_db)  # Esto asegura que los cambios persistan
        session.commit()
        session.refresh(note_db)
    return {"message": "Nota actualizada", "note": note_db.model_dump()}


# Notes: Eliminar nota
@app.delete("/notes/{note_id}", tags=["Notes"])
def delete_note(note_id: int, session: SessionDep):
    note = session.get(Notes, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Notes not found")
    session.delete(note)
    session.commit()
    return {"Nota eliminada": True}
#Fin prueba metodos Notes


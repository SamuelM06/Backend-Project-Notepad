from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Annotated
from fastapi import Depends

sqlite_file_name = "BD_Proyecto.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args={"timeout": 30})

def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Alias para reutilizar la dependencia
SessionDep = Annotated[Session, Depends(get_session)]
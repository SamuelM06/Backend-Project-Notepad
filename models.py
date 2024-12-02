from typing import Union
from pydantic import BaseModel
from datetime import date
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import Depends



class User(SQLModel, table=True):
    name: str = Field(index=True)
    gmail: str | None = Field(default=None)
    password: str | None = Field(default=None, index=True)
    idu: int | None = Field(default=None, primary_key=True)

    
class Notes(SQLModel, table=True):
    title: str = Field(index=True)
    description: str | None = Field(default=None)
    date: date
    idn: int | None = Field(default=None, primary_key=True)   





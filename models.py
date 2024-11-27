from typing import Union
from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    name: str
    gmail:str
    password: float
    is_active: Union[bool, None] = False


class Notes(BaseModel):
    title: str
    descripcion: str
    date: date
    user_id: int
    
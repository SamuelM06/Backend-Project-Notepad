from typing import Union
from pydantic import BaseModel

class User(BaseModel):
    name: str
    password: float
    is_active: Union[bool, None] = False


class Notes(BaseModel):
    descripcion: str
    user_id: int
    title: str
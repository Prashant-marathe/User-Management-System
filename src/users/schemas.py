from pydantic import BaseModel
import uuid

class User(BaseModel):
    uid:uuid.UUID
    name:str
    username:str
    email:str
    role:str
    active:bool
    login_count:int

class UserCreateModel(BaseModel):
    name:str
    username:str
    email:str
    role:str
    active:bool
    login_count:int


class UserUpdateModel(BaseModel):
    name:str
    username:str
    email:str
    role:str
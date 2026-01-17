from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str
    username:str
    email:str
    role:str
    active:bool
    login_count:int

class UserCreateModel(BaseModel):
    id:int 
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
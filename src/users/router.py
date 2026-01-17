from fastapi import HTTPException, status, APIRouter
from src.users.users_data import users
from typing import List
from src.users.schemas import User, UserCreateModel, UserUpdateModel

user_router = APIRouter()

# & Get all users
@user_router.get("/", response_model=List[User])
async def get_users():
    return users

# & Get a single user
@user_router.get("/{user_id}")
async def get_user(user_id:int) -> dict:
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User Not Found')

# & Create a new user
@user_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user_data:UserCreateModel) -> dict:
    user_data = user_data.model_dump()
    users.append(user_data)
    return user_data


# & Update user data partially
@user_router.patch("/{user_id}")
async def update_user(user_id:int, user_update_data:UserUpdateModel) -> dict:
    user_update_data = user_update_data.model_dump()
    for user in users:
        if user["id"] == user_id:
            user.update(user_update_data)
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")

# & Delete existing user
@user_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id:int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
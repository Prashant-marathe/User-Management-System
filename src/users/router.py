from fastapi import HTTPException, status, APIRouter, Depends
from typing import List
from src.users.schemas import User, UserCreateModel, UserUpdateModel
from src.users.service import Service
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.database import get_session

user_router = APIRouter()
user_service = Service()

# & Get all users
@user_router.get("/", response_model=List[User])
async def get_users(session:AsyncSession = Depends(get_session)):
    users = await user_service.get_all_users(session)
    return users

# & Get a single user
@user_router.get("/{user_uid}", response_model=User)
async def get_user(user_uid:str, session:AsyncSession = Depends(get_session)):
    user = await user_service.get_user(user_uid, session)
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User Not Found')

# & Create a new user
@user_router.post("/", status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user(user_data:UserCreateModel, session:AsyncSession = Depends(get_session)) -> dict:
    new_user = await user_service.create_user(user_data, session)
    return new_user


# & Update user data partially
@user_router.patch("/{user_uid}", response_model=User)
async def update_user(user_uid:str, user_update_data:UserUpdateModel, session:AsyncSession = Depends(get_session)):
    updated_user = await user_service.update_user(user_uid, user_update_data, session)
    if updated_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    return updated_user

# & Delete existing user
@user_router.delete("/{user_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_uid:str, session:AsyncSession = Depends(get_session)):
    user_to_delete = await user_service.delete_user(user_uid, session)

    if user_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    return {}
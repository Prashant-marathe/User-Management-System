from sqlmodel import select, desc
from sqlalchemy.ext.asyncio import AsyncSession
from src.users.models import User
from src.users.schemas import UserCreateModel, UserUpdateModel


class Service:

    # & Get all Users
    async def get_all_users(self, session:AsyncSession):
        statement = select(User).order_by(desc(User.created_at))
        result = await session.execute(statement)
        return result.scalars().all()

    # & Create new user
    async def create_user(self, user_data:UserCreateModel, session:AsyncSession):
        user_data = user_data.model_dump()

        new_user = User(
            **user_data
        )
        session.add(new_user)
        await session.commit()
        return new_user
    
    # & Get a single user
    async def get_user(self, user_uid:str, session:AsyncSession):
        statement = select(User).where(user_uid == User.uid)
        result = await session.execute(statement)
        return result.scalar()

    # & Update existing user
    async def update_user(self, user_uid:str, user_update_data:UserUpdateModel, session:AsyncSession):
        user = await self.get_user(user_uid, session)
        user_update_data = user_update_data.model_dump()

        for k,v in user_update_data.items():
            setattr(user, k, v)

        await session.commit()

        return user
    
    # & Delete user
    async def delete_user(self, user_uid:str, session:AsyncSession):
        user = await self.get_user(user_uid, session)
        await session.delete(user)
        await session.commit()

        return {}


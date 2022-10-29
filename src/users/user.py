from fastapi import APIRouter, HTTPException
from beanie import PydanticObjectId
from typing import List

from data_access.models import User


user_router = APIRouter()


@user_router.get("/")
async def get_all_user() -> List[User]:
    users = await User.find_all().to_list()

    return users

@user_router.get("{user_id}")
async def retrieve_user(user_id: PydanticObjectId) -> User:
    user = await User.get(user_id)
    if user:
        return user
    return {"Message": f"User not found by this id {user_id}"}

@user_router.post("/")
async def create_user(user: User) -> User:
    await user.create()

    return {"Message": "User is created successfully"}

from datetime import datetime

from beanie import Document, PydanticObjectId
from pydantic import Field


class Blog(Document):
    title: str = Field(max_length=200)
    description: str = Field(max_length=400)
    like_count: int = 0
    created_at: datetime = datetime.now()

    class Settings:
        name: str = "Blogs database"
    
    class Config:
        schema_extra = {
            "title": "Blog title",
            "description": "Blog description",
            "created_at": datetime.now()
        }

class User(Document):
    name: str = Field(max_length=50)
    email: str = Field(max_length=50)
    password: str = Field(max_length=20)
    created_at: datetime = datetime.now()

    class Settings:
        name: str = "Users database"
    
    class Config:
        schema_extra = {
            "name": "username",
            "email": "example@example.com",
            "password": "somepassword",
            "created_at": datetime.now()
        }

class Like(Document):
    user: PydanticObjectId
    blog: PydanticObjectId
    created_at: datetime = datetime.now()
    is_liked: bool = True

    class Settings:
        name: str = "Likes database"

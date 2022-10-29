from fastapi import APIRouter, HTTPException

from beanie import PydanticObjectId
from typing import List

from data_access.models import Blog, User, Like


blog_router = APIRouter()


@blog_router.get("/", status_code=200)
async def get_all_blogs() -> List[Blog]:
    blogs = await Blog.find_all().to_list()
    return blogs


@blog_router.get("/{blog_id}", status_code=200)
async def get_blog(blog_id: PydanticObjectId) -> Blog:
    blog = await Blog.get(blog_id)
    if blog is not None:
        return blog
    return {"Mesage": "Blog not found"}

@blog_router.post("/create", status_code=201)
async def create_blog(blog: Blog) -> Blog:
    await blog.create()

    return {"Mesage": "Blog is created successfully"}

@blog_router.delete("/{blog_id}", status_code=204)
async def delete_blog(blog_id: PydanticObjectId):
    deleted_blog = await Blog.get(blog_id)
    if deleted_blog is not None:
        deleted_blog.delete()
        return {"Message": "Blog deleted"}
    return {"Message": "Blog not found"}

@blog_router.put("/{blog_id}", status_code=204)
async def update_blog(blog_id: PydanticObjectId, blog: Blog) -> Blog:
    updated_blog = await Blog.get(blog_id)
    if updated_blog is None:
        raise HTTPException(
            status_code=404,
            detail= "Blog not found"
        )
    updated_blog.title = blog.title
    update_blog.description = blog.description
    update_blog.save()

    return updated_blog

@blog_router.post("/like_blog", status_code=201)
async def like_blog(like: Like) -> Like:
    await like.create()

    return {"Message": "Liked blog"}

@blog_router.post("/check_like_blog", status_code=200)
async def like_product(blog_id: PydanticObjectId, user_id: PydanticObjectId):
    liked_blog = await Blog.get(blog_id)
    print(liked_blog, '=--------------------------------')

    like = await Like.find_one(
        {
            "blog": blog_id,
            "user": user_id,
            "is_liked": True
        }
    )
    if like:
        await like.delete()
        liked_blog.like_count -= 1
        await liked_blog.save()
        return {"Message": f"{blog_id} id blog is disliked by {user_id} user"}


    like = Like(blog = blog_id, user = user_id)
    await Like.insert_one(like)
    liked_blog.like_count += 1
    await liked_blog.save()
    return {"Message": f"{blog_id} id blog is liked by {user_id} user"}

@blog_router.get("/all_likes", status_code=200)
async def get_all_like() -> List[Like]:
    likes = await Like.find_all().to_list()
    
    return likes

import fastapi
from fastapi import FastAPI, Body, Depends
import uvicorn

from newapp.model import PostSchema, UserSchema, UserLoginSchema
from newapp.auth.jwt_handler import signJWT
from newapp.auth.jwt_bearer import jwtBearer
posts = [
    {
        "id": 1,
        "title": "Cat",
        "content": "Cats are domestic animals."
    },
    {
        "id": 2,
        "title": "Lion",
        "content": "Lions are the king of the jungle."
    },
    {
        "id": 3,
        "title": "Dolphin",
        "content": "Dolphins are aquatic animals and are considered mammals."
    }
]

users = []

app = FastAPI(title="Authenticate")


@app.get("/", tags=["test"])
def greet():
    return {"Hello":"World"}

@app.get("/animals", tags=["posts"])
def get_posts():
    return {"data": posts}

@app.get("/animal/{id}", tags=["posts"])
def get_by_id(id: int):
    if id > len(posts):
        return {"Post with this ID doenot exists."}
    
    for post in posts:
        if post["id"] == id:
            return {"data": post}        
        
@app.post("/post_animal", dependencies=[Depends(jwtBearer())], tags=["posts"])
def post_animal(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {"Info": "Post added."}

@app.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default = None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data : UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False

@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {"Invalid" : "Invalid login details."}
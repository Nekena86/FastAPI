import datetime

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import HTMLResponse
from typing import List

from wsproto.events import TextMessage

app = FastAPI()

post_db: List[object] = []

@app.get("/ping", status_code=200)
def read_root():
    return {"message": "pong"}

@app.get("/home", status_code=200)
def read_welcome():
  return HTMLResponse("""<html>
        <h1>Welcome home!</h1>
  </html>""")


class Post(BaseModel):
    author:str
    title:str
    content:str
    creation_datetime:datetime.datetime

@app.post("/posts", status_code=201)
def create_post(post: Post):
    post_db.append(post)
    return post_db

@app.get("/posts", status_code=200)
def get_posts():
    return post_db

@app.put("/posts")
def add_post(post: Post):
    if post in post_db:
        return{"post":post}
    post_db.append(post)
    return {"post": post}


class User(BaseModel):
    username:str
    password:str

@app.get("/ping/auth")
def auth(user: User):
    if user.username == "admin" and user.password == "123456":
        return {"message":read_root()}
    else:
        return {"message": "authentification failed"}



from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Text
import uvicorn 


app = FastAPI()

posts = []

class Post(BaseModel):
    created_at : datetime = datetime.now()
    contador: int
    published: bool

@app.get('/')
def read_root():
    return {"Bienvenida: bienvenidos a mi api"}


@app.get('/post')
def get_posts():
    if len(posts) > 0:
        Post.contador = len(posts)
        return posts
    else:
        return "No hubo ninguna conexion a un endpoint"
    

@app.post('/posts')
def save_post(post: Post):
    post.append(post.dict())
    if Post.published:
        return Post.created_at
    else: 
        return datetime




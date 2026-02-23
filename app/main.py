from contextlib import asynccontextmanager
from random import randrange
from typing import Optional
import pydantic
from fastapi import FastAPI, HTTPException, Response, status
from fastapi.params import Depends
from sqlalchemy.orm import Session, defer
import models
from database import engine, SessionLocal



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("App is going to start")
    print("step1" "step2" "step3", sep=" ")

    models.Base.metadata.create_all(bind=engine)
    yield
    print("App is closing now")
    print("Good Bye")

app  = FastAPI(lifespan=lifespan)




def get_db():
    session = SessionLocal()
    yield session

class Post(pydantic.BaseModel):
    name : str
    place : str
    zipcode: Optional[int] = None

my_posts = [{"name" : "sai", "place"  :  "vemcity", "zipcode" : 516349}, {"name" : "Hema", "place"  :  "PLVD", "zipcode" : 516329}]

@app.get("/health")
def healthCheck():
    return "App is up and running"


@app.post("/upload")
def postContent(new_post : Post, response: Response):
    content = new_post.model_dump()
    print(type(content))
    content.update({ "zipcode": randrange(0,10000 )})
    my_posts.append(content)
    response.status_code=status.HTTP_201_CREATED
    return {"message" : "Posted Data Successfully", "data" : my_posts}

def get_content(zipcode):
    for i in my_posts:
        if i['zipcode'] == zipcode:
            return i
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

@app.get("/getpost/latest")
def get_latest_post():
    return my_posts[len(my_posts) - 1]

@app.get("/getpost/{zipcode}")
def get_post(zipcode: int):
    print(zipcode)
    return get_content(zipcode)


@app.delete("/deletepost/{id}")
def delete_post(id: int):
    print(id)
    for i, p in enumerate(my_posts):
        print(p)
        if p['zipcode'] == id :
            print("came inside")
            my_posts.pop(i)
            print(my_posts)
            return "Item delete from list"
    print("Coming out of loop")
    return "Item not found"

@app.get("/sqlalchemy")
def testing_db_connection(db: Session = Depends(get_db)):
    posts = db.query(models.User).all()
    return {"Message" : "Success", "data" :  posts}








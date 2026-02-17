from socket import fromfd

import fastapi
import pydantic
from typing import Optional
from random import randrange

app  = fastapi.FastAPI()

class Post(pydantic.BaseModel):
    name : str
    place : str
    zipcode: Optional[int] = None

my_posts = [{"name" : "sai", "place"  :  "vemcity", "zipcode" : 516349}, {"name" : "Hema", "place"  :  "PLVD", "zipcode" : 516329}]

@app.get("/health")
def healthCheck():
    return "App is up and running"


@app.post("/upload")
def postContent(new_post : Post):
    content = new_post.model_dump()
    print(type(content))
    content.update({ "zipcode": randrange(0,10000 )})
    my_posts.append(content)
    return {"message" : "Posted Data Successfully", "data" : my_posts}

def get_content(zipcode):
    for i in my_posts:
        if i['zipcode'] == zipcode:
            return i

@app.get("/getpost/{zipcode}")
def get_post(zipcode: int):
    print(zipcode)
    return get_content(zipcode)







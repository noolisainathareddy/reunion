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
    return {"message" : "Posted Data Successfully", "data" : content}








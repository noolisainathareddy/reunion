import fastapi
import pydantic


app  = fastapi.FastAPI()

class Post(pydantic.BaseModel):
    name : str
    place : str
    zipcode: int


@app.get("/health")
def healthCheck():
    return "App is up and running"


@app.post("/upload")
def postContent(new_post : Post):
    print(type(new_post))
    print(new_post.model_dump_json())
    return {"Posted Data Successfully"}







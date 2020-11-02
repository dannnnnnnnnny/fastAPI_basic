from enum import Enum
from fastapi import FastAPI     # 모듈 가져오기

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()                 # 인스턴스 생성

@app.get("/")                   # 경로 연산 데코레이터 정의
async def root():               # 해당 경로의 작업 기능 (async가 아닌 일반 함수로 정의도 가능)
    return {"message" : "Hello World"}  # 콘텐츠 반환

@app.get("/items/{item_id}")    # 매개 변수 선언 가능
async def read_item(item_id: int):
    return {"item_id" : item_id}

@app.get("/users/me")           # /users/me 가 /users/{user_id} 보다 먼저 선언되어야 적용될 수 있음!
async def read_user_me():
    return {"user_id" : "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

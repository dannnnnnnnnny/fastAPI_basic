# FastAPI 사용해보기!

## pip install fastapi
## pip install uvicorn

- main.py 생성 후
- uvicorn main:app --reload 로 실행
    * main : 파일 이름
    * app : main.py 라인 내부에 생성된 객체 (app = FastAPI())
    * --reload : 코드 변경 후 서버를 다시 시작함. (개발용에서만 사용)

=> localhost:8000 에서 message: "Hello World"를 확인
=> localhost:8000/docs 에서 자동으로 생성된 API 문서를 확인할 수 있음
=> localhost:8000/doc 에서 대체 문서 제공

### OpenAPI
- FastAPI는 API 정의를 위한 OpenAPI 표준을 사용하며 API로 스키마를 생성함.
- JSON Schema 사용
    => 원시 OpenAPI 스키마가 궁금하면 http://localhost:8000/openapi.json 에서 확인 가능함.

#### API 조작
- POST, GET, PUT, DELETE
- OPTIONS, HEAD, PATCH, TRACE

``` Python
from fastapi import FastAPI     # 모듈 가져오기

app = FastAPI()                 # 인스턴스 생성

@app.get("/")                   # 경로 연산 데코레이터 정의
async def root():               # 해당 경로의 작업 기능 (async가 아닌 일반 함수로 정의도 가능)
    return {"message" : "Hello World"}  # 콘텐츠 반환

@app.get("/items/{item_id}")        # 매개 변수 선언 가능
async def read_item(item_id: int):  # 타입 힌트 가능
    return {"item_id" : item_id}    
    # localhost:8000/items/3 =>  {"item_id":3} // 문자열 입력시 내부적으로 데이터 유효성 검사 후 HTTP 오류가 표시됨.
```

#### API 경로 문제

``` Python
@app.get("/users/me")
async def read_user_me():
    return {"user_id" : "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
```

/users/{user_id} 는 모든 문자열에 대해 그대로 user_id를 반환할 수 있습니다.

/users/{user_id} 를 /users/me 보다 앞에 선언한다면, 작업은 순서대로 되기 때문에 "user_id": "me" 를 반환할 것입니다.


``` Python
from enum import Enum

class ModelName(str, Enum):     # Enum을 통해 유효한 값을 고정시키는 클래스 속성을 생성
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

...

@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):     # 클래스로 유효한 값을 고정시킴
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":             # .value를 통해 실제 값을 얻어올 수 있음
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```
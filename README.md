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
```


from fastapi import FastAPI     # 모듈 가져오기

app = FastAPI()                 # 인스턴스 생성

@app.get("/")                   # 경로 연산 데코레이터 정의
async def root():               # 해당 경로의 작업 기능 (async가 아닌 일반 함수로 정의도 가능)
    return {"message" : "Hello World"}  # 콘텐츠 반환

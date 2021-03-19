from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Jesus Mary Joseph, I love you save all souls"}

@app.get("/get")
async def get_name(name:str):
    return {"name": name}
from fastapi import FastAPI

app = FastAPI()
# to run the server -> uvicorn main:app --reload

@app.get("/")
async def root():
    return {"message": "Hello World"}
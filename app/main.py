"""FastAPI basic app"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """root endpoint"""
    return {"message": "Hello World"}

import os
from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
def read_root():
    return {"response": "Hello World"}

@app.get("/random")
def random_number():
    return {"random_number": random.randint(0, 100)}

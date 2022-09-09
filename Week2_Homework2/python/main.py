from fastapi import FastAPI, Query
from datetime import datetime
import requests
import random


app = FastAPI()


@app.get("/")
def _():
    return {"Hello: World"}


@app.get("/items")
def _(page: int = Query(default=1, gt=0)):
    return {"page": page}

@app.get("/items/{item_id}")
def _(item_id: int):
    return {"item_id": item_id}


@app.get("/getdate")
def _():
    today = datetime.now()
    iso_date = today.isoformat()
    return iso_date

@app.get("/nodedate")
def _():
    response = requests.get("http://127.0.0.1:3000/timestamp")
    print(response.content)
    return "This is the Node Server's Date", response.content

@app.get("/nodelen")
def _():
    response = requests.get("http://127.0.0.1:3000/getlength")
    print(response.content)
    return "The Node Server sends the length of a string: ", response.content


@app.get("/convertBin")
def _():
    randomInt = random.randint(0,100)
    print(randomInt)
    return randomInt, " converted into binary is: ", bin(randomInt)
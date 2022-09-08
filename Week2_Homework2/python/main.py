from urllib import response
from fastapi import FastAPI  
from datetime import datetime
import requests
import random


app = FastAPI()


@app.get("/")
def _():
    return {"Hello: World"}


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
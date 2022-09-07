from fastapi import FastAPI  
from datetime import datetime
import requests


app = FastAPI()


@app.get("/")
def _():
    return {"Hello: World"}


@app.get("/getdate")
def _():
    today = datetime.now()
    iso_date = today.isoformat()
    print('Today Datetime:', today)
    print('Today Datetime:', iso_date)
    return iso_date
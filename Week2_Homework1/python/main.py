import json
import csv
from urllib import response
from fastapi import FastAPI  
import requests

app = FastAPI()   

@app.get("/goku") 
async def main_route():     
  return {"message": "Hey, It is me Goku"}

@app.get("/")
def _():
    response = requests.get("http://127.0.0.1:3000/endpoint")
    print(response.content)
    return response.content

@app.get("/aboutme")
def _():
    about = ""
    data = {}
    with open('aboutme.csv', 'r') as f:
        csvReader = csv.DictReader(f)

        for rows in csvReader:
            key = rows['id']
            data[key] = rows
    return data


@app.get("/message")
def _():
    messageString = ""
    data = {}
    with open("message.txt", 'r') as f:
        i = 0
        for rows in f:
            data[i] = rows
            i = i + 1
        messageString = json.dumps(data, indent=2)
        print(messageString)
    return data


@app.get("/test")
def _():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url)
    print(response.text)
    return response.text



from fastapi import FastAPI
import json
app = FastAPI()

"""
HTTP Method :
--> GET : To Just shows or Display any message on the website or the page on the application
"""

@app.get("/")
def greet():
    return {"message": "Hello, World!"}

@app.get("/hello")
def hello():
    return "This is Hello page from FastAPI"

def get_data():
    with open("student.json", "r") as file:
        return json.load(file)

@app.get("/students")
def get_students():
    data = get_data()
    return data


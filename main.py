from fastapi import FastAPI, HTTPException, Path
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

def load_data():
    with open("student.json", "r") as file:
        return json.load(file)

@app.get("/students")
def get_students():
    data = load_data()
    return data

@app.get("/students/{student_id}")
def get_student(student_id: str = Path(..., description="The ID of the student to retrieve")):
    data = load_data()
    if student_id not in data:
        raise HTTPException(
            status_code=404, 
            detail="Student with ID {student_id} not found"
        )
    return data[student_id]


"""
http://127.0.0.1:8000:8000/
"""

@app.get('/filter')
def filter_student(course : str):
#course=Python
    data = load_data()

    if course not in data:
        return data
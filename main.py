from fastapi import FastAPI, HTTPException, Path, Query
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
QUERY-PARAMETERS :
http://127.0.0.1:8000:8000/filter?course=Python
? -> after this our query present 
course = python -> this is key value pair

"""

@app.get('/filter')
def filter_student(course : str = 
                Query(None, description="Show only students in a specific course", 
                    examples=["Python"])):
#course=Python
    data = load_data()

    if course not in data:
        return data
        
    filtered = {}
    for student_id, student_info in data.items():
        if student_info["course"].lower() == course.lower():
            filtered[student_id] = student_info

    return filtered

# http://127.0.0.1:8000/sort?sort_by=marks,age,name&order=asc,desc

SORT_FIELDS = ["marks", "age", "name"]
SORT_ORDER = ["asc", "desc"]

@app.get('/sort')
def sort_students(
    sort_by : str = Query(None, description="Sort by marks, name, age", examples=["marks"]),
    order : str = Query(None, description="Sort order asc or desc", examples=["asc", "desc"])
):
    if sort_by not in SORT_FIELDS:
        raise HTTPException(status_code=404, detail=f"Invalid sort_by '{sort_by}', Choose from {SORT_FIELDS} ")

    if order not in SORT_ORDER:
        raise HTTPException(status_code=404, detail=f"Invalid order '{order}', Choose from {SORT_ORDER} ")  

    data = load_data()

    student = []
    for student_id, student_info in data.items():
        student_info["id"] = student_id
        student.append(student_info)

    # step - 2 Sort the list by the choosen field and order
    reverse = (order == "desc")
    sorted_students = sorted(student, key=lambda x: x[sort_by], reverse=reverse)

    return sorted_students

# this is the sorted student list by the choosen field and order
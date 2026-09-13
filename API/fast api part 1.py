from fastapi import FastAPI

app = FastAPI()


@app.get("/")

def test():
    return{"message": "Hello World!"}


@app.get("/raj")

def test1():
    return "my name is Rajesh"


@app.get("/raje/test/abc/xyz")

def test2():
    return "my name is Rajesh2"


students = {1:"Akash",2:"Ram",3:"Sham"}

@app.get("/stu")
def get_students():
    return students


@app.get("/stud/{stud_id}")
def student_search(stud_id:int):
    return {"id":stud_id,"name":students[stud_id]}


@app.get("/add_student")
def add_student(stud_id:int, name:str):
    students[stud_id] = name
    return students






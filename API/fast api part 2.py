from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor


app = FastAPI()

db_url = "postgresql://neondb_owner:npg_hproRL19tucf@ep-solitary-mud-ayjjrw2g-pooler.c-5.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"


class students(BaseModel):
    id: int
    name: str
    age: int


def get_connection_url():
    conn = psycopg2.connect(db_url, cursor_factory=RealDictCursor)
    return conn


def save_student_to_file(data):
    with open("students.txt", "a") as f:
        f.write(f"{data.id},{data.name},{data.age}\n")


@app.post("/students")
def create_student(stud: students):
    save_student_to_file(stud)
    return {"message": "student data saved successfully"}


@app.post("/students/db/insert")
def store_student_in_db(stud: students):        # <-- accept the body here
    conn = get_connection_url()
    cursor = conn.cursor()
    insert_query = "INSERT INTO STUDENT (id, name, age) VALUES (%s, %s, %s)"  # lowercase %s
    cursor.execute(insert_query, (stud.id, stud.name, stud.age))              # use stud, not student
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "student inserted into db successfully"}   # good practice: always return something



@app.delete("/students/db/delete/{student_id}")
def delete_student_in_db(student_id: int):
    conn = get_connection_url()
    cursor = conn.cursor()
    delete_query = "DELETE FROM STUDENT WHERE id = %s"
    cursor.execute(delete_query, (student_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "student deleted from db successfully"}



@app.post("/students/db/update")
def update_student_in_db(student_id: int, stud: students):
    conn = get_connection_url()
    cursor = conn.cursor()
    update_query = "UPDATE STUDENT SET name = %s, age = %s WHERE id = %s"
    cursor.execute(update_query, (stud.name, stud.age, student_id))
    
    if cursor.rowcount == 0:
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "no student found with that id"}
    
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "student updated in db successfully"}











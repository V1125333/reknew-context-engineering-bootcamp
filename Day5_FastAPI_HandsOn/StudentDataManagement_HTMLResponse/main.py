from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

student_data = []
auto_increment = 1

@app.get("/",response_class=HTMLResponse)
async def start_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Student Data Management"})

#Add new Student
@app.get("/add_Student", response_class=HTMLResponse)
async def add_student_form(request: Request):
    return templates.TemplateResponse(
        "add_student.html",
        {"request": request, "title": "Add New Student"}
    )
# Add new Student
@app.post("/add_Student",response_class=HTMLResponse)
async def add_student(request:Request):
    global auto_increment
    form_data = await request.form()
    name = form_data.get("name")
    age = form_data.get("age")
    grade = form_data.get("grade")

    student = {
        "id": auto_increment,
        "name": name,
        "age": age,
        "grade": grade
    }

    student_data.append(student)
    auto_increment += 1

    return templates.TemplateResponse(
        "add_student.html",
        {
            "request": request,
            "title": "Student Added Successfully",
            "student_data": student_data
        }
    )



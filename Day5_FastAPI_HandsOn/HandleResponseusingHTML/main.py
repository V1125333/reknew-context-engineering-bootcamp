from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Setting up the templates directory (relative to this file's folder at runtime)
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "title": "Welcome to FastAPI",
            "username": "Venu Madhav Pendurthi",
            "topics": ["FastAPI", "Jinja2", "HTML Responses"]
        }
    )

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import random
import os

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    number = random.randint(1, 20)
    answer = number // 2
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "number": number,
            "answer": answer
        }
    )



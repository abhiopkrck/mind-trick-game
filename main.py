from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import random

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def mind_trick(request: Request):
    # Random number to add for the trick
    number = random.randint(1, 30)
    answer = number / 2
    return templates.TemplateResponse("index.html", {
        "request": request,
        "number": number,
        "answer": answer
    })

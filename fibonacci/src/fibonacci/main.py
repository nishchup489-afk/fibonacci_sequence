from fastapi import FastAPI , Form , Response , Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os 
from pathlib import Path
from fastapi.staticfiles import StaticFiles


BASE_DIR = Path(__file__).resolve().parent
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
public_path = os.path.join(current_dir, "public")

app = FastAPI()

templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))
app.mount("/public", StaticFiles(directory=public_path), name="public")


@app.get("/" , response_class=HTMLResponse)
def Home(request: Request):
    return templates.TemplateResponse(
        name ="index.html" , 
        request= request
    )


def fibonacci(n):
    if (n<2):
        print("Number must be greater than 2.")
        return "Number must be greater than 2." , None
    
    numbers = []
    a,b = 0,1
    
    for k in range(n):
        numbers.append(a)
        a,b = b, a+b

    return numbers

@app.post("/calc"  , response_class=HTMLResponse )
def calculate(request : Request , user_input: int = Form()):
    result = fibonacci(user_input)
    return templates.TemplateResponse(
        "index.html" ,
        {
            "request" : request ,
            "result" : result
        }
    )

@app.get("/about" , response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse(
        "about.html",
        {"request" : request}
    )
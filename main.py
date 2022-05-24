import os
from typing import Optional
from fastapi import FastAPI, Depends, Security, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes import readings
from dotenv import load_dotenv
from db.connection import con

# load .env envrionment variables
load_dotenv()

# Create the app instance
app = FastAPI()
app.include_router(readings.router)
app.mount("/lib", StaticFiles(directory="lib"), name="lib")

# create a templates object
templates = Jinja2Templates(directory="views")

# fetch data from db
@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/lib/plotly")
def plotly(request: Request):
    return templates.TemplateResponse("lib/plotly.js", {"request": request})

@app.get("/test/{var}")
def test(var: str):
    return os.getenv(var)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/auth_config")
def get_auth_config(request: Request):
    return Jinja2Templates(directory="config").TemplateResponse("config.json", {"request": request})

@app.get("/auth_callback")
def auth_callback():
    return {"message": "this is the auth callback url. not protected"}

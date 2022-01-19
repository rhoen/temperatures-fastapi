import os
from typing import Optional
from fastapi import FastAPI, Depends, Security, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi_auth0 import Auth0, Auth0User
from dotenv import load_dotenv

# load .env envrionment variables
load_dotenv()

# create auth scheme using 3rd party fastapi_auth0 library (not Auth0 official)
auth = Auth0(
    domain=os.getenv('AUTH0_DOMAIN'),
    api_audience=os.getenv('AUTH0_API_AUDIENCE'),
    scopes={"read:admin": "Allowed to read admin things"}
)

# Create the app instance
app = FastAPI()

# create a templates object
templates = Jinja2Templates(directory="views")


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

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


@app.get("/api/user", dependencies=[Depends(auth.implicit_scheme)])
def api_user(user: Auth0User=Security(auth.get_user)):
    return {
        "user": {
            "id": user.id,
            "email": user.email
        },
        "secret_data": "this is a secret message"
    }

@app.get("/api/private/scopes", dependencies=[Depends(auth.implicit_scheme)])
def super_secret_scoped_stuff(user: Auth0User=Security(auth.get_user, scopes=["read:admin"])):
    """A valid access token is required to access this route"""
    return f"You found it! Only users with the read:admin privelege can be here. The user is: {user}"


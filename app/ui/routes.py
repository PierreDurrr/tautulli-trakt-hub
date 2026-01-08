from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db import SessionLocal, User

templates = Jinja2Templates(directory="ui/templates")
router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    db = SessionLocal()
    users = db.query(User).all()
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "users": users
    })

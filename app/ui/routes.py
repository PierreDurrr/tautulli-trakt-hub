from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db import SessionLocal, User
from fastapi.responses import RedirectResponse
from plex.users import sync_plex_users

templates = Jinja2Templates(directory="ui/templates")
router = APIRouter()

@router.post("/users/sync")
def sync_users():
    sync_plex_users()
    return RedirectResponse("/", status_code=303)

@router.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    db = SessionLocal()
    users = db.query(User).all()
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "users": users
    })

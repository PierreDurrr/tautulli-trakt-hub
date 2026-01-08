from fastapi import APIRouter, Request
from db import SessionLocal, User, TraktToken
from trakt.client import scrobble

router = APIRouter()

@router.post("/tautulli")
async def tautulli_webhook(request: Request):
    payload = await request.json()
    username = payload.get("user")

    db = SessionLocal()
    user = db.query(User).filter_by(plex_username=username, enabled=True).first()
    if not user:
        return {"status": "ignored"}

    token = db.query(TraktToken).filter_by(user_id=user.id).first()
    if not token:
        return {"status": "no_trakt"}

    scrobble(token, payload)
    return {"status": "ok"}

import requests
import xmltodict
from config import PLEX_TOKEN
from db import SessionLocal, User

def sync_plex_users():
    if not PLEX_TOKEN:
        raise RuntimeError("PLEX_TOKEN not set")

    r = requests.get(
        "https://plex.tv/api/users",
        headers={"X-Plex-Token": PLEX_TOKEN},
        timeout=10
    )
    r.raise_for_status()

    data = xmltodict.parse(r.text)
    plex_users = data["MediaContainer"].get("User", [])

    db = SessionLocal()

    seen_usernames = set()

    for u in plex_users:
        username = u.get("@username")
        plex_id = u.get("@id")
        managed = u.get("@home") == "1"

        if not username:
            continue

        seen_usernames.add(username)

        user = db.query(User).filter_by(plex_username=username).first()
        if not user:
            user = User(
                plex_username=username,
                plex_user_id=plex_id,
                is_managed=managed,
                enabled=not managed
            )
            db.add(user)
        else:
            user.plex_user_id = plex_id
            user.is_managed = managed

    # Disable users removed from Plex
    for user in db.query(User).all():
        if user.plex_username not in seen_usernames:
            user.enabled = False

    db.commit()

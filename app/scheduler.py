import time
from db import SessionLocal, TraktToken
from trakt.refresh import refresh_token_if_needed

def scheduler_loop():
    while True:
        db = SessionLocal()
        tokens = db.query(TraktToken).filter_by(auto_refresh=True).all()
        for token in tokens:
            refresh_token_if_needed(token)
        db.commit()
        time.sleep(1800)

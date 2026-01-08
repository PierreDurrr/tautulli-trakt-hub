import time
import requests
from config import TRAKT_CLIENT_ID, TRAKT_CLIENT_SECRET
from security import decrypt, encrypt

def refresh_token_if_needed(token):
    if token.expires_at > time.time():
        return

    r = requests.post(
        "https://api.trakt.tv/oauth/token",
        json={
            "refresh_token": decrypt(token.refresh_token),
            "client_id": TRAKT_CLIENT_ID,
            "client_secret": TRAKT_CLIENT_SECRET,
            "grant_type": "refresh_token"
        }
    )

    data = r.json()
    token.access_token = encrypt(data["access_token"])
    token.refresh_token = encrypt(data["refresh_token"])
    token.expires_at = int(time.time()) + data["expires_in"]

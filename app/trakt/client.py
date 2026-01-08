import requests
import time
from config import TRAKT_CLIENT_ID
from security import decrypt
from trakt.refresh import refresh_token_if_needed

def scrobble(token, payload):
    refresh_token_if_needed(token)

    headers = {
        "Authorization": f"Bearer {decrypt(token.access_token)}",
        "trakt-api-version": "2",
        "trakt-api-key": TRAKT_CLIENT_ID
    }

    data = {
        "progress": payload.get("progress", 0)
    }

    requests.post("https://api.trakt.tv/scrobble/start", headers=headers, json=data)

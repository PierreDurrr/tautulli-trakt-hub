import os

BASE_URL = os.getenv("BASE_URL", "http://localhost:8787")

PLEX_TOKEN = os.getenv("PLEX_TOKEN", "")
TAUTULLI_SECRET = os.getenv("TAUTULLI_SECRET", "")

TRAKT_CLIENT_ID = os.getenv("TRAKT_CLIENT_ID", "")
TRAKT_CLIENT_SECRET = os.getenv("TRAKT_CLIENT_SECRET", "")

DB_PATH = "/config/app.db"

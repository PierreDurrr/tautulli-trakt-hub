import requests
import xmltodict
from config import PLEX_TOKEN

def fetch_plex_users():
    r = requests.get(
        "https://plex.tv/api/users",
        headers={"X-Plex-Token": PLEX_TOKEN}
    )
    data = xmltodict.parse(r.text)
    return data["MediaContainer"]["User"]

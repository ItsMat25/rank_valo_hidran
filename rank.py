import os
import requests

API_KEY = "HDEV-9b362ce3-7204-4262-b3c9-8b81091be63e"

url = "https://api.henrikdev.xyz/valorant/v2/mmr/eu/Hidrann/832"
headers = {"Authorization": API_KEY}

res = requests.get(url, headers=headers).json()

if "data" in res:
    current = res["data"]["current_data"]

    text = f"{current['currenttierpatched']} - {current['ranking_in_tier']} RR"

    path = os.path.join(os.path.dirname(__file__), "rank.txt")

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    print(text)
else:
    print("Erreur API :", res)
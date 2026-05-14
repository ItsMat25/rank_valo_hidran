import requests

RIOT_NAME = "Hidrann"
RIOT_TAG = "832"
REGION = "eu"

url = f"https://api.henrikdev.xyz/valorant/v1/mmr/{REGION}/{RIOT_NAME}/{RIOT_TAG}"

data = requests.get(url).json()

rank = data["data"]["currenttierpatched"]
rr = data["data"]["ranking_in_tier"]

text = f"🔥 {rank} - {rr} RR"

with open("rank.txt", "w", encoding="utf-8") as f:
    f.write(text)

print(text)
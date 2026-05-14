import os
import time

repo = r"C:\Users\mathe\Bureau\Projet\H\Twitch_RankUpdater\rank_valo_hidran"
os.chdir(repo)

while True:
    os.system("python rank.py")

    # évite crash lock
    try:
        os.system("git add rank.txt")
        os.system('git commit -m "update rank"')
        os.system("git push")
    except:
        print("Git bloqué, skip cycle")

    time.sleep(300)
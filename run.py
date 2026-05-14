import os
import time

while True:
    os.system("python rank.py")
    os.system("git add rank.txt")
    os.system('git commit -m "update rank"')
    os.system("git push")

    time.sleep(300)
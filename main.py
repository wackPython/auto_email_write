import keyboard
import time

YOUR_EMAIL = "ex : email@examle.com"
YOUR_KEY = "ex: maj"

while True:
    if keyboard.read_key() == YOUR_KEY:
        keyboard.write(YOUR_EMAIL)
        time.sleep(2)
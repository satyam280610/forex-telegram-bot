import requests
import time
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

offset = None

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": text
    })

print("Bot started...")

while True:
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    params = {"timeout": 30, "offset": offset}
    response = requests.get(url, params=params).json()

    if "result" in response:
        for update in response["result"]:
            offset = update["update_id"] + 1

            if "message" in update:
                text = update["message"]["text"]

                if text == "/start":
                    send_message("🤖 Bot is active.")

                elif text == "/help":
                    send_message("Available commands:\n/start\n/help")

    time.sleep(1)

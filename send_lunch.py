import requests

def send_lunch(token, chat_id, text):
    requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}")


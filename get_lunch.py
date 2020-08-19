from bs4 import BeautifulSoup
import requests
from datetime import datetime

def get_lunch():
    soup = BeautifulSoup(requests.get("https://ravintolapalvelut.iss.fi/espoon-tietokylä").text, "html.parser")
    days = soup.find_all("div", "lunch-menu__day", limit=5)
    weekday = datetime.today().weekday()
    return days[weekday].get_text().strip()

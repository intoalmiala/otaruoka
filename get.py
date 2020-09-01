from bs4 import BeautifulSoup
import requests
from datetime import datetime

def get_lunch():
    today = datetime.today()
    weekno = today.isocalendar()[1]
    weekday = today.weekday()
    soup = BeautifulSoup(requests.get("https://ravintolapalvelut.iss.fi/espoon-tietokylä/lukiolaisten-lounaslista-viikko-" + str(weekno)).text, "html.parser")
    strings = list(map(lambda x: x.get_text(), filter(lambda x: len(x.string.strip()), soup.find("div", "article__body").contents)))
    menu = [strings[i]+'\n'+strings[i+1]+'\n'+strings[i+2] for i in range(0,15,3)]
    return menu[weekday]

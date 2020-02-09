import requests
from bs4 import BeautifulSoup

URL = "https://www.instagram.com/{}/"


def scrape(username):
    full_url = URL.format(username)
    r = requests.get(full_url)
    s = BeautifulSoup(r.text, "lxml")

    tag = s.find("meta", attrs={"name": "description"})
    text = tag.attrs['content']
    main_text = text.split("-")[0]

    return main_text


USERNAME = "amazing.python"
data = scrape(USERNAME)
print(data)

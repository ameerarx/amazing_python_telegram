# Scrape общее количество случаев,смертей,выздоровевших
import requests 
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus"
r = requests.get(url)
s = BeautifulSoup(r.text,"html.parser")
data = s.find_all("div",class_ = "maincounter-number")

print("Подтвержденные случаи: ",data[0].text.strip())
print("Летальные исходы: ",data[1].text.strip())
print("Выздоровело: ",data[2].text.strip())


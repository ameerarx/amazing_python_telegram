import requests
from bs4 import BeautifulSoup

def scrape(link):
    data =  [] # Список для хранение данных
    link = link + '/videos' # Перейти к видео
    r = requests.get(link) # Отправить get запрос
    s = BeautifulSoup(r.text,'lxml') # Скормить BeautifulSoup
    # Найти все видео и просмотреть 3 видео
    for i in s.find_all('h3',class_= "yt-lockup-title")[:3]:
        title = i.a.attrs['title'] # захватить ссылку и название
        v_link = "https://www.youtube.com"+i.a.attrs['href']
        data.append((title,v_link)) # добавить в список
    return data

# Ссылка на любой канал YouTube
LINK = "https://www.youtube.com/user/spacexchannel"
data = scrape(LINK)
print(data)
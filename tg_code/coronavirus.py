import requests 
from bs4 import BeautifulSoup
from plyer import notification
import time

# Функция для получения информации
res = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(res,'html.parser')
soup.encode('utf-8')
cases = soup.find("div",{"class":"maincounter-number"}).get_text().strip()

# Функция для уведомления
def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        timeout = 5
    )
while True:
    notifyMe('Total number',cases)
    time.sleep(10)

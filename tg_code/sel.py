# @pythonamazing(Telegram)

from selenium import webdriver
import time 

driver = webdriver.Chrome(executable_path = "C:\Program File (x86)\Google\Chrome\chromedriver.exe")

driver.get("https://www.instagram.com/")
refreshrate = int(10)

while True:
    time.sleep(refreshrate)
    driver.refresh()
import bs4
import requests
from selenium import webdriver
import os
import time

chromeDriverPath = 'D:/Desktop/HTML/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(chromeDriverPath)

search_URL = "https://www.google.com/search?q=bus&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiL3Y2S4_j5AhXOCt4KHQ_iDooQ_AUoAXoECAEQAw&biw=1920&bih=937&dpr=1"
driver.get(search_URL)

time.sleep(3)

a = input("waiting for user input to start")

#Scrolling all the way up
driver.execute_script("window.scrollTo(0,0);")

page_html = driver.page_source
pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
containers = pageSoup.findAll('div',{'class':"bRMDJf islir"})

len_containers = len(containers)
print("Found %s image containers"%(len_containers))


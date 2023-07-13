from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget
import requests as req
from pytube import YouTube
from concurrent.futures import ThreadPoolExecutor   # 加入 concurrent.futures 內建函式庫

#影片數量
vid_num = 30
#存放資料夾
keyword = "Video_test"

#執行
driver_path = 'E:/Desktop/HTML/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get("https://www.youtube.com/results?search_query=frc+robot")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="text"]'))
    )

for i in range(15):
    # driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);") #google
    driver.execute_script("scrollBy(0,10000)") #youtube
    time.sleep(1)

path = os.path.join(keyword)
os.mkdir(path)
count = 1
imgs = driver.find_elements_by_id("video-title")
last_video = ""
srcVid = []

for img in imgs:
    if count <= vid_num:
        try:
            img_link = img.get_attribute("href")
            if last_video != img_link and img_link!=None:
                # print(img_link)
                srcVid.append([f'{img_link}', count, keyword])
                count += 1
                last_video = img_link
            else:
                last_video = img_link
        except:
            pass
    else:
        break

def download_Video(url):
    yt = YouTube(url[0])
    print('download...')
    yt.streams.filter().get_highest_resolution().download(filename=f'{url[2]}/{url[2]}_{url[1]}.Mp4')
    # 下載最高畫質影片，如果沒有設定 filename，則以原本影片的 title 作為檔名
    print('ok!')

print(srcVid)

executor = ThreadPoolExecutor()          # 建立非同步的多執行緒的啟動器
with ThreadPoolExecutor() as executor:
    executor.map(download_Video,srcVid)     # 同時下載圖片
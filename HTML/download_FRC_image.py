from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget
import requests as req
from concurrent.futures import ThreadPoolExecutor   # 加入 concurrent.futures 內建函式庫

#照片數量
img_num = 700
#資料夾名稱
keyword = "scenery"

ori_url = 'https://www.google.com/search?q=%E9%A2%A8%E6%99%AF&source=lnms&tbm=isch&sa=X&ved=2ahUKEwipg_2UlYP8AhUECKYKHTnVAnQQ_AUoAXoECAEQAw&biw=1920&bih=937&dpr=1'

#執行
img_num =img_num+1
driver_path = 'E:/Desktop/HTML/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get(ori_url)

# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "rg_i"))
# )

for i in range(3):
    driver.execute_script("scrollBy(0,10000)")  # youtube
    time.sleep(1.5)
    try:
        more = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input'))
        )
        more.click()
    except:
        pass

path = os.path.join(keyword)
# os.mkdir(path)
count = 1
img_urls = []


for i in range(1,img_num):
    try:
        img_ori = driver.find_element_by_xpath(f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img')#.screenshot(f'D:/Desktop/HTML/#frcrobot/frc{i}.png')
        src_ori = img_ori.get_attribute("src")
        img_ori.click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img')))
        img = driver.find_element_by_xpath('//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img')
        img_link = img.get_attribute("src")

        print(img_link)

        if img_link == src_ori:
            img.screenshot(f'E:/Desktop/HTML/{keyword}/{keyword}_{i}.png')
            time.sleep(2)
        else:
            img_urls.append([f'{img_link}', i])
    except:
        pass

def download(url):                     # 編輯下載函式
    # print(url)                           # 印出網址
    jpg = req.get(url[0])           # 使用 requests.get 取得圖片資訊
    f = open(f'{keyword}/{keyword}_{url[1]}.jpg', 'wb')    # 將圖片開啟為二進位格式 ( 請自行修改存取路徑 )
    f.write(jpg.content)                 # 存取圖片
    print('download')
    f.close()
    print('ok')

# print(img_urls)
executor = ThreadPoolExecutor()          # 建立非同步的多執行緒的啟動器
with ThreadPoolExecutor() as executor:
    executor.map(download, img_urls)     # 同時下載圖片



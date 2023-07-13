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

img_ori = driver.find_element_by_xpath(f'//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')#.screenshot(f'D:/Desktop/HTML/#frcrobot/frc{i}.png')
src_ori = img_ori.get_attribute("src")
img_ori.click()
time.sleep(2)
print(src_ori)
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img')))
img = driver.find_element_by_xpath('//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img')
img_link = img.get_attribute("src")

print(img_link)




# import gdown
#
#
#
# a = "https://drive.google.com/open?id=1k7GzxBXDsg4WNiT-k4X8IFz2BCYD0mjF"
# # x = a.split("id=")
# # y = x[1]
# # path = f"drive.google.com/u/5/uc?id={y}&export=download"
# gdown.download("https://drive.google.com/u/5/uc?id=1fKDdzddLvTTUgS3ZWWATeOtlytFMTWGy&export=download", 'D:/Desktop/a.ipt')
#
# "drive.google.com/u/5/uc?id=14XaKlzCVlaUA_HrbB3VmJ2C-Dwm-wsJ8&export=download"


import gdown
import os
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://drive.google.com/u/1/uc?id=1oQ4EKcrsLArdZQoML3ZDJBmBU01hjYE7&export=download"
os.chdir('D:\Desktop')
# gdown.download(url)

driver_path = 'D:/Desktop/HTML/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(driver_path)

driver.get(url)

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="uc-download-link"]'))
)
username.click()



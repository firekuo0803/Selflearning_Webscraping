from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget
import bs4
import requests as req

driver_path = 'E:/Desktop/HTML/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(driver_path)

# driver.get("https://www.facebook.com/")
driver.get('https://fb.watch/jObsah2H3L/')

login2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="login_form"]/div[1]/a/div[1]/div/span/span'))
)

login2.click()

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="pass"]'))
)

login = driver.find_element_by_name("login")
username.clear()
password.clear()
# username.send_keys("blackfirefirefire0803@gmail.com")
username.send_keys("")
password.send_keys("")
login.click()
time.sleep(10)

next = True

# talk = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@id="watch_feed"]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[3]'))
#     )
# talk.click()
num = 446
keyword = "auto_test"
while next:

    talk2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="watch_feed"]/div/div[1]/div/div/div[2]/div[3]/div[2]/div/div[2]/div[1]/form/div/div[1]/div/div/div[1]/p'))
    )

    talk2.send_keys(f'{keyword}{num}')

    send = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="focused-state-composer-submit"]/span/div'))
    )
    send.click()
    num = num + 1
    time.sleep(0.3)
# time.sleep(1)
# search.send_keys(Keys.RETURN)
# time.sleep(1)
# search.send_keys(Keys.RETURN)
#222222
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "rg_i"))
# )
#
# for i in range(5):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(1)
# more = WebDriverWait(driver, 10).until(
# EC.presence_of_element_located((By.XPATH, '//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input'))
# )
# more.click()
# for i in range(5):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(1)
# imgs = driver.find_elements_by_class_name("rg_i")
# time.sleep(1)
# #22222
#
# keyword = "frc2"
# path = os.path.join(keyword)
# os.mkdir(path)
# count = 0
#
# # for img in imgs:
# #
# #     save_as = os.path.join(path, keyword+str(count)+".jpg")
# #     print(img.get_attribute("src"))
# #     wget.download(img.get_attribute("src"), save_as)
# #     count +=1
#
# for i in range(1,10):
#     try:
#         img_ori = driver.find_element_by_xpath(f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img')#.screenshot(f'D:/Desktop/HTML/#frcrobot/frc{i}.png')
#         img_ori.click()
#         time.sleep(2)
#         WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.XPATH, "//*[@id=\"Sva75c\"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img")))
#         img = driver.find_element_by_xpath("//*[@id=\"Sva75c\"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img")
#         img_link = img.get_attribute("src")
#         print(img_link)
#         save_as = os.path.join(f'D:/Desktop/HTML/{keyword}', keyword + str(i) + ".jpg")
#         wget.download(img_link, save_as)
#     except:
#         pass


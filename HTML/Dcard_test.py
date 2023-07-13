from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = 'E:/Desktop/HTML/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(driver_path)

driver.get("https://www.dcard.tw/f")
print(driver.title)
search = driver.find_element_by_name("query")
search.clear()
search.send_keys("比特幣")
search.send_keys(Keys.RETURN)

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "sc-f860e6e9-1"))
)

titles = driver.find_elements_by_class_name("sc-8fe4d6a1-3")
for title in titles:
    print(title.text)

link = driver.find_element_by_link_text("狂買比特幣的薩爾瓦多一年後竟然是？")
link.click()
driver.back()
driver.forward()

time.sleep(5)
# driver.quit()
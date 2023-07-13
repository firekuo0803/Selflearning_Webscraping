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
import math

#照片數量
img_num = 100
#資料夾名稱
keyword = "ani"

ori_url = 'https://www.facebook.com/login.php?skip_api_login=1&api_key=274266067164&kid_directed_site=0&app_id=274266067164&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fapp_id%3D274266067164%26auth_type%26cbt%3D1686838690794%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df27bb78b6b75%2526domain%253Dwww.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.pinterest.com%25252Ff2eaaf406e5d70c%2526relation%253Dopener%26client_id%3D274266067164%26config_id%26display%3Dpopup%26domain%3Dwww.pinterest.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.pinterest.com%252Fsearch%252Fpins%252F%253Fq%253D%2525E6%2525BC%2525AB%2525E7%252595%2525AB%252520%2525E5%2525A5%2525B3%252520%2525E9%2525A0%2525AD%2525E5%252583%25258F%2526rs%253Dguide%2526add_refine%253D%2525E6%2525BC%2525AB%2525E7%252595%2525AB%252520%2525E5%2525A5%2525B3%25257Cguide%25257Cword%25257C10%26force_confirmation%3Dfalse%26id%3Df37a14eed01f678%26locale%3Dzh_TW%26logger_id%3D394cbdd9-cde5-424c-8e14-e47a38a2e4e9%26messenger_page_id%26origin%3D1%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df13ba0860dea3d4%2526domain%253Dwww.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.pinterest.com%25252Ff2eaaf406e5d70c%2526relation%253Dopener.parent%2526frame%253Df37a14eed01f678%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%252Cuser_friends%26sdk%3Djoey%26size%3D%257B%2522width%2522%253A600%252C%2522height%2522%253A679%257D%26url%3Ddialog%252Foauth%26version%3Dv12.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df13ba0860dea3d4%26domain%3Dwww.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.pinterest.com%252Ff2eaaf406e5d70c%26relation%3Dopener.parent%26frame%3Df37a14eed01f678%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=zh_TW&pl_dbl=0'


#執行
img_num =img_num+1
driver_path = 'E:/Desktop/HTML/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get(ori_url)
print('1')
time.sleep(1)

def cl (xp):
    c = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xp))
    )
    c.click()

def ent (xp, word):
    e = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xp))
    )
    e.clear()
    e.send_keys(word)

ent('//*[@id="email"]',"")
ent('//*[@id="pass"]', '')
cl('//*[@id="loginbutton"]')
time.sleep(6)

ori_url = 'https://www.pinterest.com/search/pins/?q=%E6%BC%AB%E7%95%AB%20%E5%A5%B3%20%E9%A0%AD%E5%83%8F&rs=guide&add_refine=%E6%BC%AB%E7%95%AB%20%E5%A5%B3%7Cguide%7Cword%7C10'
driver.get(ori_url)
time.sleep(12)
#
# # cl('//*[@id="__PWS_ROOT__"]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/button/div/div')
# # cl('//*[@id="__PWS_ROOT__"]/div/div[1]/div[3]/div/div/div/div/div/div[4]/div[1]/div[1]/div/div/div/span/iframe')

ori_url = 'https://www.pinterest.com/search/pins/?q=%E6%BC%AB%E7%95%AB%20%E5%A5%B3%20%E9%A0%AD%E5%83%8F&rs=guide&add_refine=%E6%BC%AB%E7%95%AB%20%E5%A5%B3%7Cguide%7Cword%7C10'
driver.get(ori_url)
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="mweb-unauth-container"]'))
# )
time.sleep(3)

# for i in range(20):
#     driver.execute_script("scrollBy(0,10000)")  # youtube
#     time.sleep(1.5)
#     # try:
#     #     more = WebDriverWait(driver, 10).until(
#     #     EC.presence_of_element_located((By.XPATH, '//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input'))
#     #     )
#     #     more.click()
#     # except:
#     #     pass

if not os.path.isdir(keyword):
    os.mkdir(keyword)
path = os.path.join(keyword)
# os.mkdir(path)
count = 1
img_urls = []
print('2')
scroll = 0
x = True
y = 1

for i in range(1,img_num):

    while x == True:
        try:
            c = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH,
                                                f'//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[2]/div/div/div[4]/div/div[1]/div/div/div/div[1]/div[{y}]/div/div/div/div/div/div[1]/div[1]/a/div/div[1]/div/div/div/div/div/img'))
            )
            x = False

            break

        except:
            scroll = scroll + 150
            driver.execute_script(f'window.scrollTo(0,{scroll})')

    x = True

    # try:
    img = driver.find_element_by_xpath(f'//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[2]/div/div/div[4]/div/div[1]/div/div/div/div[1]/div[{y}]/div/div/div/div/div/div[1]/div[1]/a/div/div[1]/div/div/div/div/div/img')

    img_link = img.get_attribute("src")
    width = img.get_attribute("naturalWidth")
    height = img.get_attribute("naturalHeight")

    loss = abs(int(width)-int(height))
    print(f'epoch:{i} w:{width} h:{height} loss:{loss}')

    if loss <= 10:
        img_urls.append([f'{img_link}', i])
    else:
        # print('no')
        pass
    y = y+1
    if y == 27:
        y =1
        scroll = scroll + 100
        driver.execute_script(f'window.scrollTo(0,{scroll})')
    # except:
    #     print('no')
    #     pass

print(img_urls)

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



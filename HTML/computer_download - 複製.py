from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget
from concurrent.futures import ThreadPoolExecutor   # 加入 concurrent.futures 內建函式庫
import bs4
import requests as req

#基本設定--------------------------
driver_path = 'D:/Desktop/HTML/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(driver_path)
vdo_xpath = '//*[@id="my-video_html5_api"]'

driver.get("https://www.lccnet.tv/pages/result.aspx")

src_list = []

i = 8
i_ori = i
j = 2
j_ori = j
x1 = 0
save_dir = 'D:/Desktop/computer_learning/'
last_title = ''

def downloadVDO(link):
    print('downloading')
    try:
        os.mkdir(save_dir+link[0])
    except:
        pass
    try:
        os.mkdir(save_dir + f'{link[0]}/{link[3]}')
    except:
        pass
    save_path = save_dir+f'{link[0]}/{link[3]}/{link[1]}.txt'

    if os.path.exists(save_path) == False:
        # r = req.get(link[2])
        # with open(save_path, mode='wb') as file:
        #     file.write(r.content)
        # wget.download(link[2], save_path)
        f = open(save_path, 'w')
        f.write(link[2])
        f.close()

def click_table(xpath):
    tar = driver.find_element_by_xpath(xpath)
    tar.click()

#登入------------------------
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_header1_LoginHyperLink"]'))
)

login = driver.find_element_by_xpath('//*[@id="ctl00_header1_LoginHyperLink"]')
login.click()

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_login1_IdTextBox"]'))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_login1_PasswordTextBox"]'))
)
log = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_login1_OKButton"]')

username.clear()
password.clear()
username.send_keys("")
password.send_keys("")
log.click()

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="aspnetForm"]/div[3]/table[2]/tbody/tr/td[2]/div'))
)

#取得大小標題與影片連結-------------------
while True:
    try:
        if i <10:
            i_name = '0' + str(i)
        else:
            i_name = str(i)

        big_title = f'//*[@id="ctl00_ContentPlaceHolder1_categorymenu1_DataList2_ctl{i_name}_TitleLabel"]'
        big_title = driver.find_element_by_xpath(big_title)
        big_title = big_title.text
        print(big_title)

        while True:
            if j < 10:
                j_name = '0' + str(j)
            else:
                j_name = str(j)

            path_title = f'//*[@id="ctl00_ContentPlaceHolder1_categorymenu1_DataList2_ctl{i_name}_DataList3_ctl{j_name}_TitleHyperLink"]'
            # if j > j_ori:
            #     break
            try:
                print(path_title)
                a = driver.find_element_by_xpath(path_title)
                medium_title = a.text
                print(medium_title)
                a.click()
                username = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="aspnetForm"]/div[3]/table[2]/tbody/tr/td[2]/div'))
                )
                while True:
                    try:
                        for t in range(1,5):
                            for q in range(1, 4):
                                vdo2 = driver.find_element_by_xpath(f'//*[@id="ctl00_ContentPlaceHolder1_resultlist3columns1_DataList1"]/tbody/tr[{t}]/td[{q}]/div/div[2]/div[1]/a')
                                vdo2.click()

                                username = WebDriverWait(driver, 10).until(
                                    EC.presence_of_element_located(
                                        (By.XPATH, '//*[@id="aspnetForm"]/div[3]/table[1]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]'))
                                )

                                small_title = '//*[@id="ctl00_ContentPlaceHolder1_player1_FormView1"]/tbody/tr/td/div[1]/h1'
                                small_title = driver.find_element_by_xpath(small_title)
                                small_title = small_title.text
                                print(small_title)

                                vT = driver.find_element_by_xpath(vdo_xpath)
                                src = vT.get_attribute("src")
                                print(src)
                                src_list.append([big_title, small_title, src, medium_title])
                                driver.back()
                                username = WebDriverWait(driver, 10).until(
                                    EC.presence_of_element_located(
                                        (By.XPATH, '//*[@id="ctl00_header1_LoginHyperLink"]'))
                                )

                        click_table('//*[@id="ctl00_ContentPlaceHolder1_resultlist3columns1_DataList1_ctl12_lastpage"]')
                        username = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="ctl00_header1_LoginHyperLink"]'))
                        )
                    except:
                        # driver.get("https://www.lccnet.tv/pages/result.aspx")
                        username = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_header1_LoginHyperLink"]'))
                        )
                        print(src_list)
                        executor = ThreadPoolExecutor()  # 建立非同步的多執行緒的啟動器
                        with ThreadPoolExecutor() as executor:
                            executor.map(downloadVDO, src_list)
                        src_list = []
                        break

            except:
                j = 0
                break

            j+=1
        i += 1

        # if i > 10:
        #     i = 0
        #     j = 2
        # if i == 2 and j == 0:
        #     break
        # if i > i_ori:
        #     executor = ThreadPoolExecutor()  # 建立非同步的多執行緒的啟動器
        #     with ThreadPoolExecutor() as executor:
        #         executor.map(downloadVDO, src_list)
        #     break
    except:
        break
print('finish_download')




import requests as req
import os
from concurrent.futures import ThreadPoolExecutor   # 加入 concurrent.futures 內建函式庫

X = 200 ##你要的照片數量

filename = "ani_img6" ##存放資料夾名稱
os.mkdir(filename)
y = [1, 2, 3, 4, 5]

def download_anime(Y):
    for i in range(X):
        url = 'https://iw233.cn/API/Random.php'

        r = req.get(url)

        with open(f'{filename}/good{X*(Y-1)+i}.jpg', mode='wb') as file:
            file.write(r.content)
        print(r.content)

executor = ThreadPoolExecutor()          # 建立非同步的多執行緒的啟動器
with ThreadPoolExecutor() as executor:
    executor.map(download_anime, y)     # 同時下載圖片

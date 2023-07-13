import os
# os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用

from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=UFarTDONR48")
print('download...')
yt.streams.filter().get_highest_resolution().download(filename='Take Me Home, Country Roads.mp4')
# 下載最高畫質影片，如果沒有設定 filename，則以原本影片的 title 作為檔名
print('ok!')
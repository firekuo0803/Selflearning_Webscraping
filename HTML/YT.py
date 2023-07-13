import requests
import tqdm
from tqdm import tqdm
import re
from pprint import pprint

headers = {
    
}
url2 = 'https://rr3---sn-un57sn7y.googlevideo.com/videoplayback?expire=1688375171&ei=IzuiZNq2IreU2roPiNqg6Ak&ip=123.204.13.43&id=o-AP2xybMQrstbVy-sNy4kWyiUZVf2S9fHOIV7bKDSwwk_&itag=248&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=rn&mm=31%2C26&mn=sn-un57sn7y%2Csn-npoe7nsy&ms=au%2Conr&mv=m&mvi=3&pl=24&initcwndbps=1157500&siu=1&spc=Ul2Sq_J-AjhKgewdeVPG95V1RIL9PzFUFvTRy83Qdmdpz4j0_Byo8mc&vprv=1&svpuc=1&mime=video%2Fwebm&ns=yv1DM_pQZnnOTuhGKH12D2QO&gir=yes&clen=27418547&dur=197.997&lmt=1653578324367999&mt=1688353285&fvip=2&keepalive=yes&fexp=24007246%2C24362685%2C24363391&c=WEB&txp=1437434&n=o_-sNOqP8DfTv3_&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Csiu%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAJ7BnbUCdmpD0rJ-O4beFbYFVQneyHfxSmUO8ZuA_ZXAAiBgqU8gRbgSO7OO9-rLm60baNi0kAK6vDmPLQc7oYpNXQ%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAOyZ8TBBIIMghXacrdNmUmdL2ayize65WJ4PUTmQllhbAiEAy1h9wj19h70q_P9L7V8Hu0To9i8qDuYI5_TrEhp2-98%3D'
video = requests.get(url2, stream = True)
print('ok')
file_size = float(video.headers.get('Content-Length'))
print(type(file_size))
video_pbar = tqdm(total = file_size)
with open('good1.mp4', mode ='wb') as f:
    for video_chunk in video.iter_content(1024*1024*2):
        f.write(video_chunk)
        video_pbar.set_description(f'downloading...')
        video_pbar.update(1024*1024*2)
    video_pbar.set_description('download_ok')
    video_pbar.close()
# with open('good.jpg', mode ='wb') as file:
#     file.write(r2.content)
#     print('download')
# print(r2.content)
# open('2.mp4', mode = 'wb').write(json_data)
# for data in json_data['resource_response']['data']['results']:
#     img_url = data['images']['orig']['url']
#     print(img_url)

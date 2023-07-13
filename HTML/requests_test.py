import requests as req
url2 = 'https://rr5---sn-npoldn7l.googlevideo.com/videoplayback?expire=1688373976&ei=eDaiZKarG_zg2roP6baXyAQ&ip=123.204.13.43&id=o-ALVEdRlL6_3WQajJ9itsQTCdacpx5GJ8hPVVyf8Eq7pE&itag=136&aitags=134%2C136%2C160%2C243%2C298%2C299&source=youtube&requiressl=yes&siu=1&spc=Ul2Sq2Sgk-qzP8xWfK-6IBnUSce2bvTvlVZV-C1NnBNWAYcLG1jkg7g&vprv=1&svpuc=1&mime=video%2Fmp4&ns=IgjxPJX_0vmDe2Y07bEPgRQO&gir=yes&clen=53968847&dur=1349.499&lmt=1685657356356441&keepalive=yes&fexp=24007246,24362685,24363391&c=WEB&txp=6216224&n=PbfJ7pLoBpwf64_&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Csiu%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgWZyE4OYhfOwBdvVKLi3TjcFA-jFX6k6QUByvHxKtiX4CIQDlzqgnUWJ1xSpgHZxduze2_l1pucZBhGtf0Gv3vrggKw%3D%3D&redirect_counter=1&cm2rm=sn-un5k7l&req_id=2f45a9ac20b7a3ee&cms_redirect=yes&cmsv=e&mh=Q5&mm=34&mn=sn-npoldn7l&ms=ltu&mt=1688352053&mv=m&mvi=5&pl=24&lsparams=mh,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRgIhAK7prosJXQMelgn9pTp9cR6RD64LN0AzWgYMGhhlv-AuAiEA_CJragHp9oWLgJDXL0UCncji5nwUWztQZDV-4uxOawA%3D'

url = 'https://hengsuyang.tingmao.com.tw/upload/images/article/202112011220553545168.jpeg'
r = req.get(url2)
f = open('2.mp4', 'wb')    # 將圖片開啟為二進位格式 ( 請自行修改存取路徑 )
f.write(r.content)                 # 存取圖片
print('download')
f.close()
print('ok')

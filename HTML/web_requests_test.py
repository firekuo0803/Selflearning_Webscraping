import requests as req

url ="https://tva1.sinaimg.cn/large/ec43126fgy1h33mlhtnb4j21do2asx6q.jpg"
r = req.get(url)

with open('good.jpg', mode ='wb') as file:
    file.write(r.content)
print(r.content)
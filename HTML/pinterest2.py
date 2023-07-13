import requests
from pprint import pprint

headers = {


}
url = 'https://www.pinterest.com/resource/BaseSearchResource/get/'
json_data = requests.get(url, headers=headers).json()
# pprint(json_data)

for data in json_data['resource_response']['data']['results']:
    img_url = data['images']['orig']['url']
    print(img_url)

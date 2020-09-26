import requests, json
""" 
r = requests.post(url+'company/add_friend/', data={'id': zid, 'com_key': com_key})

# 这一步将返回值转成json

key = json.loads(r.text) """




r = requests.get('https://api.apiopen.top/getJoke', params={'page': 1, 'count': 2})

# 这一步将返回值转成json

key = json.loads(r.text)
print(key, key['code'])
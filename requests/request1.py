import requests
url = 'https://sogou.com/web'
kw = input('enter a word:')
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
}
param={
    'query':kw
}
res = requests.get(url=url,params=param,headers=headers)
print(res.text)
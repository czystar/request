import requests
import json
url = 'https://fanyi.baidu.com/sug'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
}
word = input('请输入你所需要翻译的单词:')
param={
    'kw': word
}
res = requests.get(url=url,params=param,headers=headers)

res_dict = res.json()

#json格式存储
with open('%s'%word,'w',encoding='utf-8')as f:
    json.dump(res_dict,f,ensure_ascii=False)
    f.close()


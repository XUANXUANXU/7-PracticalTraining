import urllib.request
import kdlRandomHandler
import ssl
import requests

#使用代理发送请求

#首先从数据库中随机获取一个ip
handler = kdlRandomHandler.RandomIpHandler()
ip = handler.get_random_ip()
print(ip)

#构建一个ip地址
proxy = ip['proxy']
print(proxy)

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
}

#目标url
url = 'https://www.jianshu.com/p/b2fbf5edf051'

#设置代理参数
proxies = {'https': proxy}

#requests模块使用代理写法
response = requests.get(url, proxies=proxies,headers=headers)
if response.status_code == requests.codes.ok:
    print('使用'+proxy+"请求成功")
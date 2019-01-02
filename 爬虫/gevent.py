from gevent import monkey,pool
import gevent,requests
import lxml.etree as etree

# 有耗时操作时需要
monkey.patch_all()  # 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块


def download(url):
    print(url+'正在下载1')
    header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    response = requests.get(url,headers=header)
    print(len(response.text),url+'已完成１')

def download2(url):
    print(url+'正在下载2')
    header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    response = requests.get(url,headers=header)
    print(len(response.text),url+'已完成2')

pool = pool.Pool(2)

gevent.joinall(
    [
        pool.spawn(download,'https://www.yahoo.com/'),
        pool.spawn(download,'https://www.taobao.com/'),
        pool.spawn(download,'https://github.com/'), 
        pool.spawn(download2,'https://www.yahoo.com/'),
        pool.spawn(download2,'https://www.taobao.com/'),
        pool.spawn(download2,'https://github.com/'), 
    ]
)
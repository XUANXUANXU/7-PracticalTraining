from gevent import monkey,pool
import gevent
import requests

monkey.patch_all()

def downloadone(url):
    print('开始下载1:',url)
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    reponse = requests.get(url,headers = headers)
    print(reponse.status_code,len(reponse.text),url,'下载完毕1')

def downloadtwo(url):
    print('开始下载2:',url)
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    reponse = requests.get(url,headers = headers)
    print(reponse.status_code,len(reponse.text),url,'下载完毕2')


#定义一个协成池

pool = pool.Pool(3)

gevent.joinall(
    [
        pool.spawn(downloadtwo,'https://app.yinxiang.com/'),
        pool.spawn(downloadone,'https://www.taobao.com/'),
        pool.spawn(downloadtwo,'https://www.yahoo.com/'),
        pool.spawn(downloadone,'https://www.github.com/'),
        pool.spawn(downloadtwo,'https://www.taobao.com/'),
        pool.spawn(downloadone,'https://union-click.jd.com'),
    ]
)

协程：其实就是方法的切换，一旦执行到耗时的操作，
就切换任务，一旦耗时的操作执行完毕，就返回继续执行





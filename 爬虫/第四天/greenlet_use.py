from greenlet import greenlet
import requests

def downlaod1():
    print('执行下载请求１')
    url = 'https://www.github.com/'
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    response = requests.get(url,headers=headers)
    glt2.switch()
    print(response.status_code)
    print('下载完成1')
    glt2.switch()


def downlaod2():
    print('执行下载请求２')
    url = 'https://www.github.com/'
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    response = requests.get(url,headers=headers)
    glt1.switch()
    print(response.status_code)
    print('下载完成2')


glt1 = greenlet(downlaod1)
glt2 = greenlet(downlaod2)

glt1.switch()
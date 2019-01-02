import gevent
import requests
import time

def downloadImage(taskid):
    print('正在下载第'+str(taskid)+'张图片')

    url = 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1922364256,2465666760&fm=200&gp=0.jpg'
    header = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    redponse = requests.get(url,headers=header)
    gevent.sleep(2)
    print('下载完成'+str(taskid)+'张图片')
    with open('image'+str(taskid)+'.jpg','wb') as file:
        file.write(redponse.content)


glt1 = gevent.spawn(downloadImage,1)
glt2 = gevent.spawn(downloadImage,2)
glt3 = gevent.spawn(downloadImage,3)
glt4 = gevent.spawn(downloadImage,4)
glt5 = gevent.spawn(downloadImage,5)

glt1.join()
glt2.join()
glt3.join()
glt4.join()
glt5.join()
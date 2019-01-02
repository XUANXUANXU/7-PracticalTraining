import pymysql
import random
import re,time
import requests
import threading
from requests.exceptions import ProxyError,ConnectionError,SSLError,ReadTimeout,ConnectTimeout

test_url = 'https://www.baidu.com/'
timeout = 5

class RandomIpHandler:
    #初始化构造函数
    def __init__(self):
        
        self.client = pymysql.Connect('localhost','root','zxcvbnm000','kdlproxy',3306)
        self.cursor = self.client.cursor(cursor=pymysql.cursors.DictCursor)
        self.results = []
        self.thread = threading.Thread(target=self.get_proxy_from_db)
        #保证实例化对象之后，调用get_random_ip方法之前，
        #self.results　列表中是有值的
        self.get_data()
        self.thread.start()

    def get_proxy_from_db(self):

        while True:
            self.get_data()
            time.sleep(180)

    def get_data(self):
        #查询数据库中的所有数据
        select_SQL= 'select * from usedproxies'
        self.cursor.execute(select_SQL)
        #返回一个结果列表
        self.results=self.cursor.fetchall()
    
    def get_random_ip(self):
        if len(self.results) > 0:
            #从中随机获取一个Ip
            result=random.choice(self.results)
            status,time = self.ipCheck(result)
            if status == True:
                print(result)
                #该代理可用，返回结果
            	return result
            else:
                #如果获取的ip不可用，继续获取，直到可用为止
                self.get_random_ip()
                # 优化在这里我们可以做一个优化处理判断当前选取的ip是否可以使用
                # 优化点：如果判断当前的代理不可用，那么我们是否可以将数据库里面的这条数据删除掉
                #　将不可用的ip从可用的表中删除
                

    def ipCheck(self, ip_item):
        """代理检测"""
        proxy = ip_item['proxy']
        try:
            proxies = {
                'https': proxy
            }
            start_time = time.time()
            response = requests.get(test_url, timeout=timeout, proxies=proxies)
            if response.status_code == requests.codes.ok:
                end_time = time.time()
                used_time = end_time - start_time
                # print('Proxy Valid'+proxy, 'Used Time:', used_time)
                return True, used_time
        #出现异常则代理不可用
        except (ProxyError, ConnectTimeout, SSLError, ReadTimeout, ConnectionError):
            # print('Proxy Invalid:', proxy)
            return False, None

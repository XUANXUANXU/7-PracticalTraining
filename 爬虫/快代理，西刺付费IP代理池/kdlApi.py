#https://dev.kdlapi.com/api/getproxy/?orderid=934119499154762&num=100&area=%E5%9B%BD%E5%86%85&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=2&method=2&an_ha=1&sp2=1&quality=1&dedup=1&format=json&sep=1
import pymysql
import re,time,json
import requests
from requests.exceptions import ProxyError,ConnectionError,SSLError,ReadTimeout,ConnectTimeout

test_url = 'https://www.baidu.com/'
timeout = 10

class Spider_IP:
    def __init__(self):
        self.client = pymysql.Connect('localhost','root','zxcvbnm000','kdlproxy',3306)
        self.cursor = self.client.cursor()
    
    def get_ip_data(self):

        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
        }
        url = 'http://api3.xiguadaili.com/ip/?tid=559673411922600&num=100&delay=3&category=2&protocol=https&exclude_ports=8090,8123&filter=on'
        # #发起请求(可以),获取响应
        response = requests.get(url,headers=headers)
        # # #获取html源码(生成的是一个文本)
        html = response.text

        print(html)

        # json_data = json.loads(html)

        # print(json_data)

        # proxy_list = json_data['data']['proxy_list']
        # html = '106.14.206.26:8118|171.221.170.167:53281|163.125.235.124:8118|163.125.250.189:8118|113.200.27.10:36708|61.164.39.68:53281|61.142.72.150:33270|163.125.235.74:8118|222.184.254.170:8888|119.5.0.39:1133|171.37.153.208:8123|139.196.110.205:80|123.57.84.116:8118|183.129.207.80:41258|140.207.50.246:52574|60.208.32.201:80|118.89.138.129:59460|182.61.33.62:8118|183.129.207.84:41545|182.88.178.119:8123|61.183.176.122:57210|47.93.4.104:80|117.114.149.66:53281|58.48.168.166:51430|124.193.135.242:59138|163.125.235.143:8118|211.159.171.58:80'
        proxy_list = [i.replace('\r','') for i in html.split('\n')]
        
        print(proxy_list)

        for proxy in proxy_list:
            if len(proxy) > 0:
                #将获取的所有HTTPS协议类型的并且是高匿ip，存放进数据库
                ip_item = [proxy, 'https']
                self.save_all_ip_todb(ip_item)
                #检测代理是否可用
                status,result = self.ipCheck(proxy)
                #返回结果为True代表可用
                if status == True:
                    #将可用ip存放进数据库
                    self.save_used_ip_todb(ip_item)

        self.get_ip_data()


    def ipCheck(self, proxy):
        """代理检测"""
        print('正在检测：',proxy)
        try:
            proxies = {
                'https': proxy
            }
            start_time = time.time()
            response = requests.get(test_url, timeout=timeout, proxies=proxies)
            print(response.status_code)
            if response.status_code == requests.codes.ok:
                end_time = time.time()
                used_time = end_time - start_time
                print('Proxy Valid'+proxy, 'Used Time:', used_time)
                return True, used_time
        #出现异常则代理不可用
        except (ProxyError, ConnectTimeout, SSLError, ReadTimeout, ConnectionError):
            print('Proxy Invalid:', proxy)
            return False, None


    def save_used_ip_todb(self,ipitem):
        print(ipitem)
        print('正在保存可用代理'+ipitem[0])
        #构建数据库插入语句
        insert_sql = """
        INSERT INTO usedproxies(proxy,type) VALUES(%s,%s)
        """
        self.cursor.execute(insert_sql,ipitem)
        self.client.commit()

    def save_all_ip_todb(self,ipitem):
        # print(ipitem)
        print('正在保存代理'+ipitem[0])
        #构建数据库插入语句
        insert_sql = """
        INSERT INTO allproxies(proxy,type) VALUES(%s,%s)
        """
        self.cursor.execute(insert_sql,ipitem)
        self.client.commit()
    


if __name__ == '__main__':
    spider = Spider_IP()
    spider.get_ip_data()

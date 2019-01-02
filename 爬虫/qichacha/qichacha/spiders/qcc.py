# -*- coding: utf-8 -*-
import scrapy
from qichacha.items import QichachaItem
from scrapy.http import HtmlResponse
from scrapy.http import FormRequest
from scrapy_redis.spiders import RedisSpider

class QccSpider(RedisSpider):
    name = 'qcc'
    allowed_domains = ['qichacha.com']
    #start_urls = ['https://www.qichacha.com/g_AH.html']
    redis_key = 'qcc:start_urls'

    # def start_requests(self):
    #     #可以重写这个方法，目的为了根据start_urls参数，构建Request对象
    #     for url in self.start_urls:
    #         #构造post请求
    #         # yield scrapy.FormRequest(url,formdata={},callback=self.custom_parse)
    #         #构造get请求
    #         yield scrapy.Request(url,callback=self.custom_parse)


    # def parse(self, response):
    #     pass

    def parse(self,response):
        print(response.status)
        #step1.提取公司列表页中的公司详情地址
        companies = response.xpath('//section[@id="searchlist"]')
        for company in companies:
            qccItem = QichachaItem()
            qccItem['companyName'] = company.xpath('./a/span[2]/span[1]/text()').extract_first()
            if not qccItem['companyName']:
                qccItem['companyName'] = '----'
            qccItem['companyStatus'] = company.xpath('./a/span[2]/span[2]/text()').extract_first()
            if not qccItem['companyStatus']:
                qccItem['companyStatus'] = '----'
            qccItem['legalPerson'] = ''.join(
                company.xpath('./a/span[2]/span[2]/small[1]/text()[2]').extract()).replace(' ', '').replace('\n', '')
            if not qccItem['legalPerson']:
                qccItem['legalPerson'] = '----'
            qccItem['publishTime'] = ''.join(
                company.xpath('./a/span[2]/span[2]/small[1]/text()[4]').extract()).replace(' ', '').replace('\n', '')
            if not qccItem['publishTime']:
                qccItem['publishTime'] = '----'
            qccItem['registerCapital'] = ''.join(
                company.xpath('./a/span[2]/span[2]/small[1]/text()[6]').extract()).replace(' ', '').replace('\n', '')
            if not qccItem['registerCapital']:
                qccItem['registerCapital'] = '----'
            qccItem['industry'] = ''.join(company.xpath('./a/span[2]/span[2]/small[1]/text()[8]').extract()).replace(' ', '').replace('\n', '')
            if not qccItem['industry']:
                qccItem['industry'] = '----'
            qccItem['adress'] = ''.join(company.xpath('./a/span[2]/span[2]/small[2]/text()').extract()).replace(' ','').replace('\n', '')
            if not qccItem['adress']:
                qccItem['adress'] = '----'
            qccItem['phoneNum'] = '13457687878'
            qccItem['webUrl'] = 'www.qichacha.com'
            qccItem['email'] = 'zxsdfghj@qq.com'
            qccItem['active'] = '营业'
            qccItem['socialCode'] = 'zxcvbnsdfghjk34567'
            qccItem['taxpayerNum'] = 'asdfghjcvbnrtyu34567'
            qccItem['orginalNum'] = 'sdfghrty34567'
            qccItem['companyType'] = '餐饮'
            qccItem['registerOffice'] = '管理局'
            qccItem['cbNum'] = 3
            qccItem['peopleNum'] = 200
            qccItem['busnissTime'] = '2099'
            url = 'https://www.qichacha.com' + company.xpath('./a[1]/@href').extract_first()
            yield scrapy.Request(url,callback=self.parse_company_detail,meta={'item':qccItem})


        #step2.获取当前页面中其他分页地址
        other_page = response.xpath('//ul[@class="pagination pagination-md"]/li/a/@href').extract()
        for pageurl in other_page:
            # pageUrl = 'https://www.qichacha.com' + pageurl
            pageUrl = response.urljoin(pageurl)
            yield scrapy.Request(pageUrl,callback=self.parse)

        #step3,提取其他分类页面的地址
        other_tags = response.xpath('//dl[@class="filter-tag clearfix"]/dd/a/@href').extract()
        for tagurl in other_tags:
            # tagUrl = 'https://www.qichacha.com' + tagurl
            tagUrl = response.urljoin(tagurl)
            #errback同样是设置一个回调函数，假如请求发生错误，会回调这个方法
            yield scrapy.Request(tagUrl,callback=self.parse)


    def parse_company_detail(self,response):

        print(response.status)

        # with open('page.html','w') as file:
        #
        #     file.write(response.text)

        #在这个方法中获取公司的详情信息
        qccItem = QichachaItem()
        #
        #
        #有矿中情况，一种获取到了详情的页面源码,还有一种没有获取到页面源码
        if '企查查' in response.text:
        # if response.text.find('企查查') > 0
            # 公司名称：
            qccItem['companyName'] = response.xpath('//div[@class="content"]//h1/text()').extract_first()
            if not qccItem['companyName']:
                qccItem['companyName'] = '----'
            # status(企业状态)
            qccItem['companyStatus'] = response.xpath('//span[@class="ntag  text-success "]/text()').extract_first()
            if not qccItem['companyStatus']:
                qccItem['companyStatus'] = '----'
            # 电话号码
            qccItem['phoneNum'] = ''.join(response.xpath('//div[@class="content"]/div[@class="row"][1]/span[@class="fc "]//span[@class="cvlu"]//a/text()').extract()).replace(' ','').replace('\n','')
            if not qccItem['phoneNum']:
                qccItem['phoneNum'] = '----'
            # 官网
            qccItem['webUrl'] = response.xpath('//div[@class="content"]/div[@class="row"][1]/span[@class="cvlu "]/a/@href').extract_first()
            if not qccItem['webUrl']:
                qccItem['webUrl'] = '----'
            # 邮箱
            qccItem['email'] = ''.join(response.xpath('//div[@class="content"]/div[@class="row"][2]/span[@class="fc "]//span[@class="cvlu"]//a/text()').extract()).replace(' ','').replace('\n','')
            if not qccItem['email']:
                qccItem['email'] = '----'
            # 地址（cvlu）
            qccItem['adress'] = response.xpath('//div[@class="content"]/div[@class="row"][2]/span[@class="cvlu"]/a/text()').extract_first()
            if not qccItem['adress']:
                qccItem['adress'] = '----'
            # 法人代表
            qccItem['legalPerson'] = response.xpath('//a[@class="bname"]/h2/text()').extract_first()
            if not qccItem['legalPerson']:
                qccItem['legalPerson'] = '----'
            # 注册资本
            qccItem['registerCapital'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[1]/td[2]/text()').extract()).replace(' ','').replace('\n','')
            if not qccItem['registerCapital']:
                qccItem['registerCapital'] = '----'
            # 经营状态
            qccItem['active'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[2]/td[2]/text()').extract()).replace(' ','').replace('\n','')
            if not qccItem['active']:
                qccItem['active'] = '----'
            # 成立日期
            qccItem['publishTime'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[2]/td[4]/text()').extract()).replace(' ','').replace('\n','')
            if not qccItem['publishTime']:
                qccItem['publishTime'] = '----'
            # 社会统一信用代码
            qccItem['socialCode'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[3]/td[2]/text()').extract()).replace(' ','').replace('\n','')
            if not qccItem['socialCode']:
                qccItem['socialCode'] = '----'
            # 纳税人识别码
            qccItem['taxpayerNum'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[3]/td[4]/text()').extract()).replace(' ','').replace('\n','')
            if not qccItem['taxpayerNum']:
                qccItem['taxpayerNum'] = '----'
            # 机构代码
            qccItem['orginalNum'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[4]/td[4]/text()').extract()).replace(' ','').replace('\n','')
            if not qccItem['orginalNum']:
                qccItem['orginalNum'] = '----'
            # 公司类型
            qccItem['companyType'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[5]/td[2]/text()').extract()).replace(' ','').replace('\n','')
            if not qccItem['companyType']:
                qccItem['companyType'] = '----'
            # 所属行业
            qccItem['industry'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[5]/td[4]/text()').extract()).replace(' ','').replace('\n','')
            if not qccItem['industry']:
                qccItem['industry'] = '----'
            # 登录机关
            qccItem['registerOffice'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[6]/td[4]/text()').extract()).replace(' ','').replace('\n','')
            if not qccItem['registerOffice']:
                qccItem['registerOffice'] = '----'
            # 参保人数
            qccItem['cbNum'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[8]/td[4]/text()').extract()).replace(' ','').replace('\n','')
            if not qccItem['cbNum']:
                qccItem['cbNum'] = '----'
            # 人员规模
            qccItem['peopleNum'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[9]/td[2]/text()').extract()).replace(' ','').replace('\n','')
            if not qccItem['peopleNum']:
                qccItem['peopleNum'] = '----'
            # 营业期限
            qccItem['busnissTime'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[9]/td[4]/text()').extract()).replace(' ','').replace('\n','')
            if not qccItem['busnissTime']:
                qccItem['busnissTime'] = '----'

        else:
            qccItem = response.meta['item']
            # company = response.meta['company']
            #从company对象中获取公司信息
            
            # print('**************************')
        yield qccItem



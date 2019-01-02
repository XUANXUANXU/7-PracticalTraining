# -*- coding: utf-8 -*-
import scrapy
from qichacha.items import QichachaItem
from scrapy.http import HtmlResponse
from scrapy.http import FormRequest


class QccSpider(scrapy.Spider):
    name = 'qcc'
    allowed_domains = ['qichacha.com']
    start_urls = ['https://www.qichacha.com/g_AH.html']

    def start_requests(self):
        #可以重写这个方法，目的为了根据start_urls参数，构建Request对象
        for url in self.start_urls:
            #构造post请求
            # yield scrapy.FormRequest(url,formdata={},callback=self.custom_parse)
            #构造get请求
            yield scrapy.Request(url,callback=self.custom_parse)


    # def parse(self, response):
    #     pass

    def custom_parse(self,response):
        print(response.status)
        #step1.提取公司列表页中的公司详情地址
        companies = response.xpath('//section[@id="searchlist"]')
        for company in companies:
            url = 'https://www.qichacha.com' + company.xpath('./a[1]/@href').extract_first()
            yield scrapy.Request(url,callback=self.parse_company_detail,meta={'companySel':company})


        #step2.获取当前页面中其他分页地址
        other_page = response.xpath('//ul[@class="pagination pagination-md"]/li/a/@href').extract()
        for pageurl in other_page:
            # pageUrl = 'https://www.qichacha.com' + pageurl
            pageUrl = response.urljoin(pageurl)
            yield scrapy.Request(pageUrl,callback=self.custom_parse)

        #step3,提取其他分类页面的地址
        other_tags = response.xpath('//dl[@class="filter-tag clearfix"]/dd/a/@href').extract()
        for tagurl in other_tags:
            # tagUrl = 'https://www.qichacha.com' + tagurl
            tagUrl = response.urljoin(tagurl)
            #errback同样是设置一个回调函数，假如请求发生错误，会回调这个方法
            yield scrapy.Request(tagUrl,callback=self.custom_parse)


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
            qccItem['companyName'] = response.xpath('//div[@class="content"]//h1/text()').extract_first('暂无')
            # status(企业状态)
            qccItem['companyStatus'] = response.xpath('//span[@class="ntag  text-success "]/text()').extract_first('暂无')
            # 电话号码
            qccItem['phoneNum'] = ''.join(response.xpath('//div[@class="content"]/div[@class="row"][1]/span[@class="fc "]//span[@class="cvlu"]//a/text()').extract()).replace(' ','').replace('\n','')
            # 官网
            qccItem['webUrl'] = response.xpath('//div[@class="content"]/div[@class="row"][1]/span[@class="cvlu "]/a/@href').extract_first('暂无')
            # 邮箱
            qccItem['email'] = ''.join(response.xpath('//div[@class="content"]/div[@class="row"][2]/span[@class="fc "]//span[@class="cvlu"]//a/text()').extract()).replace(' ','').replace('\n','')
            # 地址（cvlu）
            qccItem['adress'] = response.xpath('//div[@class="content"]/div[@class="row"][2]/span[@class="cvlu"]/a/text()').extract_first('暂无')
            # 法人代表
            qccItem['legalPerson'] = response.xpath('//a[@class="bname"]/h2/text()').extract_first()
            # 注册资本
            qccItem['registerCapital'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[1]/td[2]/text()').extract()).replace(' ','').replace('\n','')
            # 经营状态
            qccItem['active'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[2]/td[2]/text()').extract()).replace(' ','').replace('\n','')
            # 成立日期
            qccItem['publishTime'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[2]/td[4]/text()').extract()).replace(' ','').replace('\n','')
            # 社会统一信用代码
            qccItem['socialCode'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[3]/td[2]/text()').extract()).replace(' ','').replace('\n','')
            # 纳税人识别码
            qccItem['taxpayerNum'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[3]/td[4]/text()').extract()).replace(' ','').replace('\n','')
            # 机构代码
            qccItem['orginalNum'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[4]/td[4]/text()').extract()).replace(' ','').replace('\n','')
            # 公司类型
            qccItem['companyType'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[5]/td[2]/text()').extract()).replace(' ','').replace('\n','')
            # 所属行业
            qccItem['industry'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[5]/td[4]/text()').extract()).replace(' ','').replace('\n','')
            # 登录机关
            qccItem['registerOffice'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[6]/td[4]/text()').extract()).replace(' ','').replace('\n','')
            # 参保人数
            qccItem['cbNum'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[8]/td[4]/text()').extract()).replace(' ','').replace('\n','')
            # 人员规模
            qccItem['peopleNum'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[9]/td[2]/text()').extract()).replace(' ','').replace('\n','')
            # 营业期限
            qccItem['busnissTime'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr[9]/td[4]/text()').extract()).replace(' ','').replace('\n','')
        else:
            companySel = response.meta['companySel']
            # 公司名称：
            qccItem['companyName'] = ''.join(companySel.xpath('.//span[@class="name"]/text()').extract())
            # status(企业状态)
            qccItem['companyStatus'] = companySel.xpath('.//span[@class="label label-success m-l-xs"]/text()').extract_first('暂无')
            # 电话号码
            qccItem['phoneNum'] = '暂无'
            # 官网
            qccItem['webUrl'] = '暂无'
            # 邮箱
            qccItem['email'] = '暂无'
            # 地址（cvlu）
            qccItem['adress'] = ''.join(companySel.xpath('.//a/span[@class="clear"]/small[2]/text()').extract())
            # 法人代表
            qccItem['legalPerson'] = '暂无'
            # 注册资本
            qccItem['registerCapital'] = '暂无'
            # 经营状态
            qccItem['active'] = '暂无'
            # 成立日期
            qccItem['publishTime'] = '暂无'
            # 社会统一信用代码
            qccItem['socialCode'] = '暂无'
            # 纳税人识别码
            qccItem['taxpayerNum'] = '暂无'
            # 机构代码
            qccItem['orginalNum'] = '暂无'
            # 公司类型
            qccItem['companyType'] = '暂无'
            # 所属行业
            qccItem['industry'] = '暂无'
            # 登录机关
            qccItem['registerOffice'] = '暂无'
            # 参保人数
            qccItem['cbNum'] = '暂无'
            # 人员规模
            qccItem['peopleNum'] = '暂无'
            # 营业期限
            qccItem['busnissTime'] = '暂无'

            #其他信息
            infos = companySel.xpath('.//small[1]/text()').extract()

            infos = [i.replace(' ','').replace('\t','') for i in infos if i != ' ']

            if len(infos) > 3:
                qccItem['legalPerson'] = infos[0]
                qccItem['publishTime'] = infos[1]
                qccItem['registerCapital'] = infos[2].replace('\n','')
                qccItem['industry'] = infos[3].replace('\n','')
            else:
                qccItem['legalPerson'] = infos[0]
                qccItem['publishTime'] = infos[1]
                qccItem['industry'] = infos[2].replace('\n','')

            #作业，把剩下的取出来
            #从companySel对象中获取公司信息

        yield qccItem



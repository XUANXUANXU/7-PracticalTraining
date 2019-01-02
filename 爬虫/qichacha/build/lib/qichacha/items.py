# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#第一目标字段
class QichachaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #公司名称：
    companyName = scrapy.Field()
    #status(企业状态)
    companyStatus = scrapy.Field()
    #电话号码
    phoneNum = scrapy.Field()
    #官网
    webUrl = scrapy.Field()
    #邮箱
    email = scrapy.Field()
    #地址
    adress = scrapy.Field()
    #法人代表
    legalPerson = scrapy.Field()
    #注册资本
    registerCapital = scrapy.Field()
    #经验状态
    active = scrapy.Field()
    #成立日期
    publishTime = scrapy.Field()
    #社会统一信用代码
    socialCode = scrapy.Field()
    #纳税人识别码
    taxpayerNum = scrapy.Field()
    #机构代码
    orginalNum = scrapy.Field()
    #公司类型
    companyType = scrapy.Field()
    #所属行业
    industry = scrapy.Field()
    #登录机关
    registerOffice = scrapy.Field()
    #参保人数
    cbNum = scrapy.Field()
    #人员规模
    peopleNum = scrapy.Field()
    #营业期限
    busnissTime = scrapy.Field()
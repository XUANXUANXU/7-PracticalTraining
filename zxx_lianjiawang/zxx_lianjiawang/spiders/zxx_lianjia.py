# -*- coding: utf-8 -*-
import scrapy
from zxx_lianjiawang.items import ZxxLianjiawangItem

class ZxxLianjiaSpider(scrapy.Spider):
    name = 'zxx_lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['http://bj.lianjia.com/']

    def parse(self, response):
        # print(response.text)
        #获取二手房和租房链接
        esf_url = response.xpath('//div[@class="nav typeUserInfo"]/ul/li[1]/a/@href').extract_first()
        zf_url = response.xpath('//div[@class="nav typeUserInfo"]/ul/li[3]/a/@href').extract_first()
        # print(esf_url,zf_url)
        yield scrapy.Request(esf_url,callback=self.zxx_esf)
        yield scrapy.Request(zf_url, callback=self.zxx_zf)
    # def parse_depail(self,response):
    #     other_tags = response.xpath('//div[@class="page-box house-lst-page-box"]/a/@href').extract()
    #     print(other_tags)
    #     for tagurl in other_tags:
    #         tagUrl = 'https://bj.lianjia.com' + tagurl
    #         print(tagUrl)
    #         yield scrapy.Request(tagUrl, callback=self.parse_depail)


        #https://bj.lianjia.com/ershoufang/pg3/

    def zxx_esf(self,response):
        item = ZxxLianjiawangItem()
        # 标题
        item['zxx_title'] = response.xpath('//ul[@class="sellListContent"]/')
        # 位置
        item['zxx_position'] = response.xpath()
        # 格局(三室两厅)
        item['zxx_pattern'] = response.xpath()
        # 面积
        item['zxx_area'] = response.xpath()
        # 采光方向(南北)
        item['zxx_direction'] = response.xpath()
        # 装修程度
        item['zxx_decoration'] = response.xpath()
        # 有无电梯
        item['zxx_elevator'] = response.xpath()
        #简介
        item['zxx_content'] = response.xpath()
        # 关注量
        item['zxx_follow'] = response.xpath()
        # 看房次数
        item['zxx_looknum'] = response.xpath()
        # 便利条件
        item['zxx_benefit'] = response.xpath()
        # 价钱
        item['zxx_money'] = response.xpath()
        # 每平方价钱
        item['zxx_square'] = response.xpath()
        # 图片链接
        item['zxx_picture'] = response.xpath()

        return item
    def zxx_zf(self,response):
        pass
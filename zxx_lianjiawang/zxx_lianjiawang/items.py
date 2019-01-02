# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZxxLianjiawangItem(scrapy.Item):
    #标题
    zxx_title = scrapy.Field()
    #位置
    zxx_position = scrapy.Field()
    #格局(三室两厅)
    zxx_pattern = scrapy.Field()
    #面积
    zxx_area = scrapy.Field()
    #采光方向(南北)
    zxx_direction = scrapy.Field()
    #装修程度
    zxx_decoration = scrapy.Field()
    #有无电梯
    zxx_elevator = scrapy.Field()
    # 简介
    zxx_content = scrapy.Field()
    #关注量
    zxx_follow = scrapy.Field()
    #看房次数
    zxx_looknum = scrapy.Field()
    #便利条件
    zxx_benefit = scrapy.Field()
    #价钱
    zxx_money = scrapy.Field()
    #每平方价钱
    zxx_square = scrapy.Field()
    #图片链接
    zxx_picture = scrapy.Field()


    #
    # zxx_follow = scrapy.Field()
    # zxx_follow = scrapy.Field()
    # zxx_follow = scrapy.Field()
    # zxx_follow = scrapy.Field()
    # zxx_follow = scrapy.Field()
    #
    # zxx_follow = scrapy.Field()
    # zxx_follow = scrapy.Field()
    #




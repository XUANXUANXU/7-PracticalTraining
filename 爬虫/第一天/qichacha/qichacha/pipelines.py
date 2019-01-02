# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
#
# class QichachaPipeline(object):
#
#     def __init__(self):
#         self.file = open('company.json','a')
#
#     def process_item(self, item, spider):
#
#         data_str = json.dumps(dict(item),ensure_ascii=False) +'\n'
#
#         self.file.write(data_str)
#
#         return item
#
#     def close_spider(self,spider):
#         self.file.close()

import pymysql

class QichachaPipeline(object):

    def __init__(self,host,port,user,pwd,db):

        self.client = pymysql.Connect(host,user,pwd,db,port,charset='utf8')
        self.cursor = self.client.cursor()


    @classmethod
    def from_crawler(cls,crawler):
        host = crawler.settings['MYSQL_HOST']
        port = crawler.settings['MYSQL_PORT']
        user = crawler.settings['MYSQL_USER']
        pwd = crawler.settings['MYSQL_PWD']
        db = crawler.settings['MYSQL_DB']

        return cls(host,port,user,pwd,db)

    def process_item(self, item, spider):

        # item.insert_data_to_db(dict(item))

        # sql,data = item.insert_data_to_db(dict(item))
        #
        # try:
        #     self.cursor.execute(sql,data)
        #     self.client.commit()
        # except Exception as err:
        #     print(err)
        #     self.client.rollback()
        return item

    def close_spider(self,spider):

        self.cursor.close()
        self.client.close()
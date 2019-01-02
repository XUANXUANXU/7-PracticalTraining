# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

# class QichachaPipeline(object):
#
#     # def __init__(self):
#         # self.file = open('company.txt','a')
#
#     def process_item(self, item, spider):
#         # data_str = json.dumps(dict(item),ensure_ascii=False) +'\n'
#         # self.file.write(dict(item))
#         with open('hhh.txt','a') as file:
#             file.write(str(item))
#         return item
     # def close_spider(self,spider):
    #     self.file.close()
import pymysql

class QichachaPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect('localhost', 'root', '199888', 'qichacha', charset="utf8")
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):

        dic = dict(item)
        table_name = 'chacha'
        sql = '''insert into %s(%s) value(%s) ''' % (table_name, ','.join([k for k in dic.keys()]), ','.join(['"' + str(v) + '"' for v in dic.values()]))
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print('插入成功')
        except:
            print('插入失败')
            self.conn.rollback()

        return item

    def close_spider(self,spider):
        self.cursor.close()




# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
import os


class CarhomePipeline(object):
    def process_item(self, item, spider):
        data = pd.DataFrame({
                'car_name': item['car_name'],
                'car_url': item['car_url'],
                'car_score': item['car_score'],
                'car_gray': item['car_gray'],
                'car_structure': item['car_structure'],
                'car_engine': item['car_engine'],
                'car_price': item['car_price']
        })
        file_path = 'f://SpiderData//汽车之家.csv'
        if os.path.exists(file_path):
            data.to_csv(file_path, encoding='ANSI', header=False, index=False, mode='a')
        else:
            data.to_csv(file_path, encoding='ANSI', header=True, index=False, mode='a')
        return item

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarhomeItem(scrapy.Item):
    # define the fields for your item here like:
    car_name = scrapy.Field()
    car_url = scrapy.Field()
    # 车辆评分
    car_score = scrapy.Field()
    # 车辆级别
    car_gray = scrapy.Field()
    # 车身结构和续航里程
    car_structure = scrapy.Field()
    # 发动机和电动机
    car_engine = scrapy.Field()
    car_price = scrapy.Field()
    pass

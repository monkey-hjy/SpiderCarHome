# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import CarhomeItem


class CarhomespiderSpider(scrapy.Spider):
    name = 'CarHomeSpider'
    start_urls = ['https://car.autohome.com.cn/#pvareaid=3311246']

    def parse(self, response):
        brand_url = response.xpath('//a[@class="item"]/@href').getall()
        for i in range(len(brand_url)):
            yield scrapy.Request('https://car.autohome.com.cn' + brand_url[i], callback=self.get_car_info)

    def get_car_info(self, response):
        car_name = response.xpath('//div[@class="main-title"]/a/text()').getall()
        car_url = response.xpath('//div[@class="main-title"]/a/@href').getall()
        # 车辆评分
        car_score = response.xpath('//span[@class="score-number"]/text()|//div[@class="score-cont"]/span/text()').getall()
        # 车辆级别
        car_gray = response.xpath('//ul[@class="lever-ul"]//li[1]/span/text()').getall()
        # 车身结构和续航里程
        car_structure = re.split('车身结构：|续航里程：', ''.join(response.xpath('//ul[@class="lever-ul"]//li[2]//text()').getall()))[1:]
        # 发动机和电动机
        car_engine = re.split('发 动 机：|电 动 机：', ''.join(response.xpath('//ul[@class="lever-ul"]//li[3]//text()').getall()))[1:]
        car_price = response.xpath('//span[@class="font-arial"]/text()').getall()
        # print('='*20, len(car_name), len(car_url), len(car_score), len(car_gray), len(car_structure), len(car_engine), len(car_price))
        item = CarhomeItem()
        item['car_name'] = car_name
        item['car_url'] = car_url
        item['car_score'] = car_score
        item['car_gray'] = car_gray
        item['car_structure'] = car_structure
        item['car_engine'] = car_engine
        item['car_price'] = car_price
        yield item

        next_url = response.xpath('//a[@class="page-item-next"]/@href').get()
        if next_url:
            yield scrapy.Request(url='https://car.autohome.com.cn' + next_url, callback=self.get_car_info)

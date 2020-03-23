# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 21:46
# @Author  : Monkey
# @File    : start.py.py
# @Software: PyCharm
# @Demand  : 启动文件

'''
{'downloader/request_bytes': 372779,
 'downloader/request_count': 1163,
 'downloader/request_method_count/GET': 1163,
 'downloader/response_bytes': 553965073,
 'downloader/response_count': 1163,
 'downloader/response_status_count/200': 1163,
 'dupefilter/filtered': 21,
 'elapsed_time_seconds': 122.824554,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2020, 3, 22, 1, 53, 13, 465216),
 'item_scraped_count': 1162,
 'log_count/DEBUG': 2326,
 'log_count/INFO': 12,
 'request_depth_max': 66,
 'response_received_count': 1163,
 'scheduler/dequeued': 1163,
 'scheduler/dequeued/memory': 1163,
 'scheduler/enqueued': 1163,
 'scheduler/enqueued/memory': 1163,
 'start_time': datetime.datetime(2020, 3, 22, 1, 51, 10, 640662)}
2020-03-22 09:53:13 [scrapy.core.engine] INFO: Spider closed (finished)
'''
from scrapy import cmdline
cmdline.execute('scrapy crawl CarHomeSpider'.split())

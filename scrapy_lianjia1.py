# -*- coding: utf-8 -*-
import scrapy
import csv
import os
import re

class LianjiaCrawlSpider(scrapy.Spider):
    name = 'lianjia_crawl'
    allowed_domains = ['sh.lianjia.com/zufang']
    start_urls = ['https://sh.lianjia.com/zufang/']
    # custom_settings={
    #     'CLOSESPIDER_ERRORCOUNT': 1
    # }

    def __init__(self):
        self.file = open('lianjia.csv', 'w',newline='')
        self.writer = csv.writer(self.file, dialect="excel")
        self.writer.writerow(['形式','小区名','区','地点','面积','朝向','户型','标签','租金','经度','纬度'])

    def start_requests(self):
        yield scrapy.Request(url='https://sh.lianjia.com/zufang',callback=self.parse_district)

    def parse_district(self, response):
        li_all = response.css('ul[data-target="area"]')
        districts = li_all.css('li a::attr(href)').extract()[1:]
        for district in districts:
            url_district='https://sh.lianjia.com'+str(district)
            yield scrapy.Request(url=url_district,callback=self.parse_block,dont_filter=True)  

    def parse_block(self, response):
        li_all = response.css('ul[data-target="area"]')
        blocks = li_all[1].css('li.filter__item--level3  a::attr(href)').extract()[1:]
        for block in blocks:
            url_block='https://sh.lianjia.com'+str(block)
            yield scrapy.Request(url=url_block,callback=self.parse_page,dont_filter=True)

    def parse_page(self, response):
        url_block = response.url
        try:
            max_page = int(response.css('div.content__pg::attr(data-totalpage)').extract()[0])
        except:
            max_page = 1
        for page in range(1,max_page+1):
            url_page=url_block+'pg'+str(page)+'/#contentList'
            yield scrapy.Request(url=url_page,callback=self.parse_dtl,dont_filter=True)

    def parse_dtl(self, response):
        li_all = response.css('div.content__list--item')
        for i in li_all:
            try:
                item = dict()
                item['title'] = i.css('p.content__list--item--title.twoline a::text').extract()[0].strip().split(' ')[0].split('·')
                item['loc'] = i.css('p.content__list--item--des a::text').extract()
                dtl = i.css('p.content__list--item--des::text').extract()[4:-1]
                dtl=[x.strip() for x in dtl]
                if len(dtl)==3:
                    item['area'], item['orientation'], item['house_type'] = dtl[0], dtl[1], dtl[2]
                elif len(dtl)==2:
                    item['area'], item['orientation'], item['house_type'] = dtl[0], '', dtl[1]
                    item['tag'] = '/'.join(i.css('p.content__list--item--bottom.oneline i::text').extract())
                    item['price'] = i.css('span.content__list--item-price em::text').extract()[0]
                    url_dtl = 'https://sh.lianjia.com'+i.css('p.content__list--item--title.twoline a::attr(href)').extract()[0]
                    yield scrapy.Request(url=url_dtl,meta={'item':item},callback=self.parse_ll,dont_filter=True)
            except:
                pass

    def parse_ll(self, response):
        item = response.meta['item']
        html = response.text
        longtitude = re.findall('longitude(.+)',html)[0]
        item['longtitude'] = re.findall('(\d+.\d+)',longtitude)[0].strip()
        latitude = re.findall('latitude(.+)',html)[0]
        item['latitude'] = re.findall('(\d+.\d+)',latitude)[0].strip()

        self.writer.writerow(
            [item['title'][0],item['title'][1],item['loc'][0],item['loc'][1],item['area'],item['orientation'],item['house_type'],item['tag'],item['price'],item['longtitude'],item['latitude']]
            )

        self.file.flush()
        os.fsync(self.file)

        print("over: " + response.url)

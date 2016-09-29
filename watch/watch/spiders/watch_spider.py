# -*- coding: utf-8 -*-
import scrapy
import boto3


class WatchSpider(scrapy.Spider):
    name = "watch"
    allowed_domains = ["bestbuy.com"]
    start_urls = (
        #'http://www.bestbuy.com/site/apple-apple-watch-38mm-stainless-steel-case-black-sports-band/4274900.p?skuId=4274900',
        'http://www.bestbuy.com/site/apple-apple-apple-watch-first-generation-38mm-stainless-steel-case-link-bracelet-link-bracelet/5581528.p?skuId=5581528',

    )

    def parse(self, response):
    	stock = response.xpath('//*[@class="availability-postcard"]/*[@class="shipping-delivery sidebar-blurb"]/*[@class="sidebar-blurb-message"]/div/text()')[0].extract()
        print stock
        if stock != ' Not Available':
        	print '38mm is' , stock
        	#sns = boto3.client('sns',region_name='us-east-1')
        	#sns.publish(PhoneNumber = '+17189264805',Message = '38mm is in stock!')

        

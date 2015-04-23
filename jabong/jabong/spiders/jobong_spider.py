from scrapy import Spider
from scrapy.http import Request
from jabong.items import JabongItem

class Jabong(Spider):

	name = 'jabong'
	start_urls = ['http://www.jabong.com/men/clothing/?source=topnav_men']
	allowed_domains = ['jabong.com']

	def parse(self,response) :

		links = response.xpath('//a[@unbxdattr="product"]/@href').extract()
		for link in links:
			yield Request(url=link, callback=self.parse_product, meta={'test':'AAAAAAAAAa'})
		#print links

	def parse_product(self,response):

		brand = response.xpath('//span[@itemprop="brand"]/text()').extract()
		price = response.xpath('//span[@id="before_price"]/span/text()').extract()[1]

		brand = brand[0] if brand else ''
		
		#price = price[0] if price else ''

		item = JabongItem(
			url = response.url,
			brand = brand,
			price = price
			)
		yield item 
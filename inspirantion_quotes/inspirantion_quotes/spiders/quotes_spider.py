from scrapy import Spider
from scrapy.http import Request
from inspirantion_quotes.items import InspirantionQuotesItem

class Quotes(Spider):

	name = 'quotes'
	start_urls = ['http://www.brainyquote.com/quotes/topics/topic_inspirational.html']
	allowed_domains = ['brainyquote.com']

	def parse(self,response):

		#NEXT_LINK =  'http://www.brainyquote.com' + response.xpath('//div[@class="pagination bqNPgn pagination-small"]/ul/li/a[contains(text(),"Next")]/@href').extract()[0]
		links = ['http://www.brainyquote.com/quotes/topics/topic_inspirational'+str(i)+'.html' for i in xrange(2,15) ]
		for link in links:
			yield Request(url=link, callback=self.parse_quote, meta={'test':'AAAAAAAAAa'})
		#print quotes

	def parse_quote(self,response):

		quotes = response.xpath('//a[@title="view quote"]/text()').extract()

		for quote in quotes: 

			item = InspirantionQuotesItem(

				quotes = quote
				)
			yield  item

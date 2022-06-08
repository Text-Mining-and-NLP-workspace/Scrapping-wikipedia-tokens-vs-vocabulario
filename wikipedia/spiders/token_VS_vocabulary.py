import scrapy
import os
from wikipedia.items import wikiItem

class ArticlesSpider(scrapy.Spider):
    name = 'token_VS_vocabulary'
    host = 'en.wikipedia.org'
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Featured_articles']
    custom_settings = {'FEEDS': {'file:'+os.getcwd()+'/token_VS_vocabulary.json':{'format': 'json','overwrite':True}}}

    def parse(self, response):
        links=response.css(".featured_article_metadata > a")
        for link in links[0:500]:
            yield scrapy.Request(f"https://{self.host}{link.attrib.get('href')}", callback=self.parse_article) 
           
    def parse_article(self, response):
        yield wikiItem(text=''.join(response.xpath('//div[@class="mw-parser-output"]//p//text()').extract()))


import scrapy
from wikipedia.items import articles,Body

class ArticlesSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Featured_articles']
    custom_settings = {'FEEDS': {'file:C:\\Users\\amuralles\\wikipedia\\articles.json':{'format': 'json','overwrite':True}}}

    def parse(self, response):
        host=self.allowed_domains[0]
        link=response.css(".featured_article_metadata > a")
        for i in range(0,25):         
            yield scrapy.Request(f"https://{host}{link[i].attrib.get('href')}", callback=self.parse_article) 
                            
    def parse_article(self, response):        
        yield articles(
            link= response.url,
            body=Body(title = response.xpath('//h1/text()').get(),
                      paragraph = ''.join(response.xpath('//div[@class="mw-parser-output"]//p[2]//text()').extract()))           
            )
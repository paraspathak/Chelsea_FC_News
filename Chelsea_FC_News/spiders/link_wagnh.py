import scrapy
from scrapy.loader import ItemLoader
from Chelsea_FC_News.items import LinksItem

class LinkWAGNH(scrapy.Spider):
    name = "links"
    start_urls = [ 'https://weaintgotnohistory.sbnation.com/']
    allowed_domains = ['https://weaintgotnohistory.sbnation.com/']
    def parse(self, response):
        for word in response.xpath("//div//h2"):
            l = ItemLoader(item = LinksItem(), selector = word)
            l.add_xpath("links_text","./a/@href")
            yield l.load_item()

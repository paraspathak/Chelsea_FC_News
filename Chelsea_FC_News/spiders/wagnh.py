import scrapy
from Chelsea_FC_News.items import WAGNHItem
from scrapy.loader import ItemLoader
class WAGNHSpider(scrapy.Spider):
    name = 'wagnh'
    start_urls = [
        'https://weaintgotnohistory.sbnation.com/'
    ]

    def parse(self, response):
        for word in response.xpath("//div[@class ='c-entry-box--compact__body']"):
            l = ItemLoader(item = WAGNHItem(), selector = word)
            l.add_xpath("wagnh_text",".//h2[@class='c-entry-box--compact__title']/a")
            yield l.load_item()

import scrapy
from ..items import AvitoCarsItem
import requests
from scrapy import Selector

class AvCarsSpider(scrapy.Spider):
    name = 'av_cars'
    page = 2
    start_urls = ['https://www.avito.ma/fr/maroc/voitures-%C3%A0_vendre']

    def parse(self, response):
        items = AvitoCarsItem()
        div = response.css('div.sc-1i02f67-0.dwiAPA')
        for res in div:
            items['car_name']= res.css('.fkzsxQ::text').extract()
            items['car_price'] = res.css('.fDAUYW span::text').extract()
            enter = res.css('div.sc-1i02f67-0.dwiAPA a::attr(href)').get()
            page2 = str(enter)
            response_2 = requests.get(page2)
            response2 = Selector(response_2)
            items['car_city'] = response2.css(".bhLody::text").extract()
            items['car_cv_man_auto'] = response2.css(".iKWYSN::text").extract()
            items['car_information'] = response2.css(".dGDJdv::text").extract()
            items['car_equipements'] = response2.css(".WhKdN::text").extract()
            yield items
        next_page = 'https://www.avito.ma/fr/maroc/voitures-%C3%A0_vendre?o=' + str(AvCarsSpider.page)
        if AvCarsSpider.page < 1000:
            AvCarsSpider.page += 1
            yield response.follow(next_page, callback=self.parse)



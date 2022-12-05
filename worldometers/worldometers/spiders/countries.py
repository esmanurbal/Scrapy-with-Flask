
import scrapy


class MyItem(scrapy.Item):
    names=scrapy.Field()
    year=scrapy.Field()
    population=scrapy.Field()
class CountriesSpider(scrapy.Spider):
    
    myBaseUrl = ''
    start_urls = []
    def __init__(self, category='', **kwargs): # The category variable will have the input URL.
        self.myBaseUrl = category
        self.start_urls.append(self.myBaseUrl)
        super().__init__(**kwargs)

    custom_settings = {'FEED_URI': 'worldometers/Outputfile.json', 'CLOSESPIDER_TIMEOUT' : 15}
    name = 'countries'
    allowed_domains = ['worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    
    def parse(self, response):

        countries=response.xpath("//td/a")
        for country in countries:
            names= country.xpath(".//text()").get()
            link= country.xpath(".//@href").get()
            yield response.follow(url=link, callback=self.country_parse, meta={'names':names})

    
    def country_parse(self, response):
        names=response.request.meta['names']
        rows= response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
    
        for row in rows:
            year=row.xpath(".//td[1]/text()").get()
            population=row.xpath(".//td[2]/strong/text()").get()
        yield MyItem(names=names,year=year,population=population)

            
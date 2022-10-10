from ast import parse
import scrapy



class PdfScrapeSpider(scrapy.Item):
    name = "ScrapePdf"
    def start_requests(self):
        start_url = ["https://www.pdfdrive.com/"]
        yield scrapy.Request(url= start_url, callback=parse)

    def parse(self,response):
        page = response.url


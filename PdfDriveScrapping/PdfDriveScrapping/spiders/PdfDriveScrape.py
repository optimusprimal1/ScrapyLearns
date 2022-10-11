# from ast import parse
import webbrowser
import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By


class PdfScrapeSpider(scrapy.Spider):
    name = "ScrapePdf"
    
    def start_requests(self):
        start_urls = ["https://www.pdfdrive.com/search?q=sports&pagecount=&pubyear=&searchin=&em="
    # "https://www.pdfdrive.com/blockchain-books.html",
    # "https://www.pdfdrive.com/animals-books.html",
    # "https://www.pdfdrive.com/food-books.html",
    # "https://www.pdfdrive.com/education-books.html"
    ]
        for url in start_urls:
            yield scrapy.Request(url= url, callback=self.parse)
    # def __init__(self):
    #     self.driver = webdriver.Firefox()



    def parse(self,response):
        # page = response.url
        # print('Checking response body= ',response.body)
        # xpath("//a[@class='ai-searcht']"))
        # print('ai-search = ', response.xpath("//a[@class='ai-search']").getall())
        for hrefs in response.xpath("//a[@class='ai-search']/@href").getall():
            print('hrefs = ', hrefs)
            yield scrapy.Request(url="https://www.pdfdrive.com"+hrefs, callback=self.get_first_downloading_page)
        
    def get_first_downloading_page(self,response):
        download_href = response.xpath("//a[@id='download-button-link']/@href").get()
        print('Entering in get_first_downloading_page = ', download_href)
        yield scrapy.Request()
    
    def downloading_files(self,response):
        print('Entering into downloading page.')



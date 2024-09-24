from scrapy import Request, Spider
from scrapy.spiders import CrawlSpider
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .items import ProductItemArtefacta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class ArtefactaSpider(CrawlSpider):
    name = "artefacta"
    allowed_domains = ["artefacta.com"]
    start_urls = [
        "https://www.artefacta.com/c/tecnologia"
    ]
    
    def start_requests(self):
        base_url = "https://www.artefacta.com/c/tecnologia?p="
        max_pages = 2  # Número máximo de páginas a recorrer

        for page_number in range(1, max_pages + 1):
            url = f"{base_url}{page_number}"
            print(f"Scrapeando la página: {url}")
            yield Request(url, callback=self.parse_page)

    def parse_page(self, response):
        # Aquí extraemos los links de productos en cada página
        product_links = response.xpath("//ol[contains(@class,'products list items product-items')]/li//h3[contains(@class,'product-item-name')]/a/@href").getall()
        
        for link in product_links:
            full_link = response.urljoin(link)  # Para asegurar que sea una URL completa
            yield Request(full_link, callback=self.parse_producto)

    def parse_producto(self, response):
        item = ProductItemArtefacta()
        try:
            title = response.xpath("//div[contains(@class,'product-brand')]//span[contains(@class,'base')]/text()").get()
            print("Title: ", title)
            item["title"] = title
            
        except Exception as e:
            print(f"Error al obtener el título: {e}")

        yield item
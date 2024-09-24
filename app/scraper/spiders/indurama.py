from scrapy  import Request, Spider
from scrapy.spiders import CrawlSpider
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from scrapy.http import HtmlResponse
from .items import ProductItemIndurama
import time


class InduramaSpider(CrawlSpider):
    name = 'indurama'
    allowed_domains = ["indurama.com"]
    start_urls = [
        'https://www.indurama.com/linea-hogar'
    ]

    def start_requests(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "translate_whitelists": {"en": "es"},
            "translate": {"enabled": "true"}
        }
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--lang=es")

        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(self.start_urls[0])
        time.sleep(5)

        xpath_element_card = '//div[@id="gallery-layout-container"]//section[contains(@class,"vtex-product-summary-2-x-container")]/a'
        url_array = []
        while True:
            try:
                # Intentar cerrar un modal si aparece
                close_button = driver.find_element(By.XPATH, '//div[@class="kevin"]')
                close_button.click()
            except:
                pass  # Si no se puede cerrar el modal, continua

            # Obtener los enlaces de cada producto
            link_elements = driver.find_elements(By.XPATH, xpath_element_card)

            for link in link_elements:
                href = link.get_attribute('href')
                print("HREF LINK : ",href)
                url_array.append(href)

            # Intentar avanzar a la siguiente página
            try:
                boton_avanzar = driver.find_element(By.XPATH, '//div[contains(@class,"container-categorymobile")]//div[contains(@class,"buttonShowMore ")]//a')
                boton_avanzar.click()
                time.sleep(2)
            except:
                print("No hay más botones 'Next' o el elemento está obsoleto. Saliendo del bucle.")
                break
        i=0
        for url in url_array:
            print("PRODUCTO : ",i)
            i=i+1 
            yield Request(url, callback=self.parse_product)


    def parse_product(self, response):
        item = ProductItemIndurama()
        try:
          title = response.xpath('//h1[contains(@class,"productNameContainer")]//span[contains(@class,"productBrand")]/text()').get()
          print("TITLE : ", title)
          item["title"] = title
        except:
          print("error")
          pass       
        
        try:
          url = response.url
          print("URL : ",url)
          item["link"] = url
        except:
          print("error")
          pass
        
        try:
          urlImg = response.xpath("//div[contains(@class,'product-main')]//div[contains(@class,'items-stretch')]//div[contains(@class,'productImage')]//img/@src").get()
          print("IMG URL : ",urlImg)
          item["link"] = urlImg
        except:
          print("error")
          pass
         
        try:
          price_parts = response.xpath("//div[contains(@class,'product-main')]//div[contains(@class,'items-stretch')]//span[contains(@class,'product-price-1-x-currencyContainer')]//span/text()").getall()
          price = ''.join(price_parts)
          print("PRICE : ",price)
          item['price'] = price
        except:
          print("error")
          pass
        try:
          description = response.xpath("//div[contains(@class,'product-main')]//div[contains(@class,'productDescriptionText')]/div/text()").getall()
          print("DESCRIPTION : ",description)
          item["description"] = description
        except:
          print("error")
          pass
        yield item

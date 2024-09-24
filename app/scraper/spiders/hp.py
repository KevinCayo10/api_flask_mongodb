from scrapy  import Request, Spider
from scrapy.spiders import CrawlSpider
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .items import ProductItemHp
import time

class HpSpider(CrawlSpider):
    name = 'hp'
    allowed_domains = ["hp.com"]
    start_urls = [
        'https://www.hp.com/ec-es/products/laptops/view-all-laptops-and-2-in-1s.html'
    ]
    max_items = 50  # Número máximo de productos que quieres scrapear

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

        xpath_element_card = '//div[@class="c-search-results__items"]//div[@class="c-product-tile__content"]//div[@class="c-product-tile__main-content"]//div[@class="c-product-tile__media-wrapper"]/a'
        url_array = []
        item_count = 0  # Contador de productos extraídos

        while item_count < self.max_items:  # Limita el número de productos
            try:
                # Intentar cerrar un modal si aparece
                close_button = driver.find_element(By.XPATH, '//div[@class="kevin"]')
                close_button.click()
            except:
                pass  # Si no se puede cerrar el modal, continúa

            # Obtener los enlaces de cada producto
            link_elements = driver.find_elements(By.XPATH, xpath_element_card)

            for link in link_elements:
                if item_count >= self.max_items:  # Verifica si se ha alcanzado el límite
                    break
                href = link.get_attribute('href')
                print("HREF LINK : ", href)
                url_array.append(href)
                item_count += 1  # Incrementar el contador de productos

            if item_count >= self.max_items:
                break

            # Intentar avanzar a la siguiente página
            try:
                boton_avanzar = driver.find_element(By.XPATH, '//div[@class="c-search-results__loadmore"]/button')
                boton_avanzar.click()
                time.sleep(2)
            except:
                print("No hay más botones 'Next' o el elemento está obsoleto. Saliendo del bucle.")
                break

        driver.quit()

        for url in url_array:
            yield Request(url, callback=self.parse_product)

    def parse_product(self, response):
        item = ProductItemHp()
        try:
            title = response.xpath('//div[contains(@class,"c-product-details__main")]//div[contains(@class,"h1")]/text()').get()
            print("TITLE : ", title)
            item["title"] = title
        except:
            print("Error al obtener el título")
            pass

        try:
            url = response.url
            print("URL : ", url)
            item["link"] = url
        except:
            print("Error al obtener la URL")
            pass

        yield item

from scrapy  import Request, Spider
from scrapy.spiders import CrawlSpider
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from scrapy.http import HtmlResponse
from .items import ProductItemMarcimex
import time


class MarcimexSpider(CrawlSpider):
    name = 'marcimex'
    allowed_domains = ["marcimex.com"]
    start_urls = [
        'https://www.marcimex.com/tecnologia'
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

          # Esperar hasta que todos los productos estén cargados
          WebDriverWait(driver, 10).until(
              EC.presence_of_element_located((By.XPATH, '//div[@id="gallery-layout-container"]'))
          )

          # Obtén todas las URLs de los productos
          url_array = []
          while True:
              try:
                  # Cerrar un modal si aparece
                  close_button = driver.find_element(By.XPATH, '//div[@class="kevin"]')
                  close_button.click()
              except:
                  pass

              link_elements = driver.find_elements(By.XPATH, '//div[@id="gallery-layout-container"]//section[contains(@class,"vtex-product-summary")]/a')
              for link in link_elements:
                  href = link.get_attribute('href')
                  if href:
                      url_array.append(href)

              try:
                  boton_avanzar = driver.find_element(By.XPATH, '//div[contains(@class,"vtex-search-result-3-x-buttonShowMore")]/a')
                  boton_avanzar.click()

                  # Esperar a que la nueva página cargue completamente
                  WebDriverWait(driver, 10).until(
                      EC.staleness_of(boton_avanzar)
                  )

                  # Esperar un poco más para asegurar la carga completa de datos
                  time.sleep(2)
              except:
                  print("No hay más botones 'Next' o el elemento está obsoleto. Saliendo del bucle.")
                  break

          for url in url_array:
              print("PRODUCTO : ", url)
              yield Request(url, callback=self.parse_product)

          driver.quit()

    def parse_product(self, response):
        # print("TEXTO  : ", response.text)
        item = ProductItemMarcimex()
      
        try:
            title_parts = response.xpath('//div[contains(@class,"Content--producto-info")]//div[contains(@class,"flexRow--nombre-prpducto")]//h1[contains(@class,"vtex-store-components-3-x-productNameContainer")]/text()').get()
      
      # Une todos los nodos de texto en una sola cadena
            title = title_parts

            #"//div[contains(@class,"Content--producto-info")]//div[contains(@class,"flexRow--nombre-prpducto")]//h1[contains(@class,"vtex-store-components-3-x-productNameContainer")]//span/text()"
            print("TITLE : ", title)
            item["title"] = title
            description = response.xpath("//div[contains(@class,'content--description-pdp')]/div/text()").getall()
            print("DESCRIPTION : ",description)
        except Exception as e:
            print("Error:", str(e))
            pass
        
        yield item


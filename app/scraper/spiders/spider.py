from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from spiders.utils.store_config import store_config 
from spiders.utils.items import ProductItem
from spiders.utils.regex import Regex


class GenericSpider(CrawlSpider):
  name = 'generic_spider'
  
  def __init__(self,store_name, *a, **kw):
    super(GenericSpider, self).__init__(*a, **kw)
    self.store_name = store_name
    self.store = store_config[self.store_name]
    self.allowed_domains = [self.store['allowed_domains']]
    self.start_urls = self.store['start_urls']
    
  def start_requests(self):
    product_urls = self.collect_product_urls()
    
    for index, url in enumerate(product_urls):
      print("Index : ", index, " - URL: ", url)
      yield Request(url, callback=self.parse_product)
 
  def collect_product_urls(self):
    chrome_options = webdriver.ChromeOptions()
    prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "translate_whitelists": {"en": "es"},
            "translate": {"enabled": "true"}
        }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--lang=es")
    driver = webdriver.Chrome(options=chrome_options)
    url_array= []
    try:
      driver.get(self.start_urls[0])
      time.sleep(15)
      xpath_element_card = self.store['product_card_xpath']
      next_button_xpath = self.store['next_button_xpath']
      
      while True:
        
        try:
          xpath_close_modal= self.store['button_close_modal_xpath']
          if xpath_close_modal:
            close_buttons = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, self.store['button_close_modal_xpath'])))
            
            for close_button in close_buttons:
              close_button.click()
        except:
          print("No modal")
        
        
        link_elements = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH, xpath_element_card)))
        
        for link in link_elements:
          href = link.get_attribute('href')
          if href not in url_array:
            url_array.append(href)
            
        try:
          next_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
          next_button.click()
          time.sleep(3)
        except:
          print("No more pages")
          break
    finally: 
      driver.quit()
    return url_array
    
    
  def parse_product(self, response):
    # ... rest of the code ...
    item = ProductItem()
    # print("PRODUCTO HTML : ", response.text)
    
    try:
      title = response.xpath(self.store['title_xpath']).get()
      item['title'] = title
    except:
      print("Error al procesar el titulo")
      
    try:
      price = response.xpath(self.store['price_xpath']).getall()
      print("PRICE : ",price)
      price_text = "".join(price)
      item['price'] = Regex.extract_precio(price_text)
    except:
      print("Error al procesar el precio")
      
    try:
      urlImg =  response.xpath(self.store['urlImg_xpath']).getall()
      item["urlImg"] =urlImg
      
    except:
      print("Error al procesar el url imagen")
      
    try:
      item["link"] = response.url
    except:
      print("Error al procesar el link")
  
    try:
      description = response.xpath(self.store['description_xpath']).getall()
      description_text = " ".join(description)
      item["description"]= description_text
      item["characteristics"] = self.process_characteristics(title, description_text)
    except:
      print("Error al procesar el descripcion")
    
    try:
      category_value = "Laptop"
      if self.store["category_xpath"] != "":
        category = response.xpath(self.store["category_xpath"]).getall()
        category_text = "".join(category)
        category_value = Regex.extract_category(category_text)
      item["category"] = category_value
    except:
      print("Error al procesar el categoria")
      
    try:
      brand = response.xpath(self.store["brand_xpath"]).getall()  
      brand_text = "".join(brand)
      item["brand"]= Regex.extract_brand(brand_text)
    except Exception as e:
      print("Error al procesar el marca", e)  
      
    try:
      stock_value = -1
      if self.store["stock_xpath"]!="":
        stock = response.xpath(self.store["stock_xpath"]).getall()
        stock_text = "".join(stock)
        stock_value = Regex.extract_stock(stock_text) if stock_text != None else -1
      item["stock"] = stock_value
    except:
      print("Error al procesar el stock")
      
    try:
      availability_value = "Stock"
      if self.store["availability_xpath"] != "":
       availability = response.xpath(self.store["availability_xpath"]).get()
       availability_value = "Stock" if availability !=None else "Agotado" 
      item["availability"] = availability_value
    except:
      print("Error al procesar disponibilidad") 
    yield item;
  
  
  def process_characteristics(self, title, description):
    print("ENTRO A EXTRAER -----------------")
    try:
      characteristics = {
        "sistema_operativo":Regex.extract_sistema_operativo(description,title),
        "procesador":Regex.extract_procesador(description, title),
        "ram":Regex.extract_ram(description, title),
        "almacenamiento":Regex.extract_almacenamiento(description,title),
        "pantalla":{
          "tamaño":Regex.extract_tamaño_pantalla(description, title),
          "tipo":Regex.extract_tipo_pantall(description),
        },
        "graficos":Regex.extract_graficos(description,title),
        "conectividad":Regex.extract_conectividad(description),
        "teclado":Regex.extract_teclado(description),
        "audio":Regex.extract_audio(description),
        "puertos":Regex.extract_puertos(description)
      }    
      return characteristics

    except Exception as e:
     print("ERROR AL REGEX : ", e)
     return None
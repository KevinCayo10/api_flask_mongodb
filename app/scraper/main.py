import sys
import os
import socketio
# Añadir el directorio 'app' al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import settings as my_settings
from spiders.utils.store_config import store_config
from spiders.spider import GenericSpider

io = socketio.Client()

def on_connect():
  print("Conexion con Flask server")
  
def on_response(data):
  print(f"Respuesta del servidor {data}")
  
io.on("connect",on_connect)
io.on("response",on_response)
def main():
    io.connect("http://localhost:5000")
    
  
    # Obtiene la configuración del proyecto Scrapy
    settings = get_project_settings()
    settings.setmodule(my_settings)

    # Configura el proceso del crawler con las configuraciones obtenidas
    process = CrawlerProcess(settings)
    
    for store_name, config in store_config.items():
            process.crawl(GenericSpider, store_name=store_name)
    process.start()
    
    io.emit("mensaje",{"status":"Scraping completado"})
    
    io.disconnect()
    # process.crawl(InduramaSpider, output='products.json', output_format='json')


if __name__ == '__main__':
    main()

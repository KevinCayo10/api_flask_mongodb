import sys
import os
import socketio
# Añadir el directorio 'app' al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.novicompu import NovicompuSpider
from spiders.hp import HpSpider
import settings as my_settings

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
    
    # Inicia el crawler con el nombre del spider
    process.crawl(NovicompuSpider)
    # # process.crawl(ArtefactaSpider)
    process.crawl(HpSpider)
    process.start()
    
    io.emit("mensaje",{"status":"Scraping completado"})
    
    io.disconnect()
    # process.crawl(InduramaSpider, output='products.json', output_format='json')


if __name__ == '__main__':
    main()

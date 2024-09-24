import sys
import os

# Añadir el directorio 'app' al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
# from app.spiders.marcimex1 import MarcimexSpider
from spiders.novicompu import NovicompuSpider
from spiders.hp import HpSpider
import settings as my_settings
def main():
    # Obtiene la configuración del proyecto Scrapy
    print("ANTES DEL PIPELINE")
    settings = get_project_settings()
    # Agrega el setting personalizado
    settings.setmodule(my_settings)
    
    process = CrawlerProcess(settings)
    
    # Inicia el crawler con el nombre del spider
    process.crawl(NovicompuSpider)
    # process.crawl(HpSpider)
    # # process.crawl(ArtefactaSpider)
    # process.crawl(HpSpider)
    process.start()
    
    # process.crawl(InduramaSpider, output='products.json', output_format='json')


if __name__ == '__main__':
    main()

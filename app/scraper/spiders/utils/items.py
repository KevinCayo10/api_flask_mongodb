import scrapy
import scrapy.item


class ProductItem(scrapy.Item):
  # define the fields for your item here like:
  # Titulo del producto
  title = scrapy.Field()
  # Precio del producto
  price = scrapy.Field()
  # Enlace del producto
  link = scrapy.Field()
  # URL de la imagen del producto
  urlImg = scrapy.Field()
  # Descripción del producto
  description = scrapy.Field()
  # Características del producto:
  """
  {
    "characteristics": {
      "procesador": "Intel Core i7-12700H",
      "ram": "16 GB DDR4",
      "almacenamiento": "512 GB SSD",
      "pantalla": {
        "tamaño": "15.6\"",
        "tipo": "IPS, Full HD (1920x1080)"
      },
      "graficos": "NVIDIA GeForce RTX 3060",
      "sistema_operativo": "Windows 11 Home",
      "teclado": "Retroiluminado, con teclado numérico",
      "conectividad": "Wi-Fi 6, Bluetooth 5.2",
      "audio": "Dolby Atmos, altavoces estéreo dual",
      "puertos": ["USB-C", "HDMI 2.0", "lector de tarjetas SD"]
    }
  }

  """
  characteristics = scrapy.Field()
  # Categoría del producto: Laptops, Computadoras, etc. 
  category = scrapy.Field()
  # Marca del producto: ASUS, HP, LENOVO, DELL
  brand = scrapy.Field()
  # Disponibilidad del producto: Disponible, No disponible
  availability = scrapy.Field()
  # Cantidades disponibles del producto
  stock = scrapy.Field()
  # Tienda enlinea
  img_store=scrapy.Field()
  
  
  
import scrapy

class ProductItemNovicompu(scrapy.Item):
   title= scrapy.Field()
   price = scrapy.Field()
   link = scrapy.Field()
   description = scrapy.Field()
   urlImg = scrapy.Field()
   
class ProductItemArtefacta(scrapy.Item):
   title= scrapy.Field()
   price = scrapy.Field()
   link = scrapy.Field()
   description = scrapy.Field()

class ProductItemMarcimex(scrapy.Item):
    title= scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    urlImg = scrapy.Field()
    
class ProductItemIndurama(scrapy.Item):
    title= scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    urlImg = scrapy.Field()
    
class ProductItemHp(scrapy.Item):
    title= scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    urlImg = scrapy.Field()
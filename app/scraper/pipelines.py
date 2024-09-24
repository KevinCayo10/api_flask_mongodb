import pymongo

class ScrapingProductosTecnologicosPipeline:
  def process_item(self, item, spider):
    return item

class MongoPipeline:
  
  collection_name = "productos_tecnologicos"
  
  def __init__(self, mongo_uri, mongo_db, mongo_collection):
    self.mongo_uri = mongo_uri
    self.mongo_db = mongo_db
    self.mongo_collection = mongo_collection
    
  @classmethod
  def from_crawler(cls, crawler):
    return cls(
      mongo_uri=crawler.settings.get('MONGODB_SERVER'),
      mongo_db=crawler.settings.get('MONGODB_DB'),
      mongo_collection=crawler.settings.get('MONGODB_COLLECTION')
    )
  
  def open_spider(self, spider):
    # Conexión a MongoDB
    self.client = pymongo.MongoClient(self.mongo_uri, tls=True, tlsAllowInvalidCertificates=True)
    self.db = self.client[self.mongo_db]
    print("Connected to MongoDB:", self.mongo_uri)
    
  def close_spider(self, spider):
    # Cierra la conexión a MongoDB
    self.client.close()
    
  def process_item(self, item, spider):
    # Inserta el item en la colección especificada
    result = self.db[self.mongo_collection].insert_one(dict(item))
    print("Inserted Item ID:", result.inserted_id)  # Muestra el ID del documento insertado
    return item

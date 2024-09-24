# def parse(self, response):
# # Obtener el HTML de la respuesta
# # html_content = response.body.decode(response.encoding)
# #truco.save_html_to_file(html_content=html_content,titulo='HTML_Adidas')
#   esNuevo = response.meta.get('esNuevo')
#   item = ZapatillaItem()
#   item['modelo'] =  response.xpath("//div[@class='content___1BnBS']//h1[@class='name___120FN']//span/text()").get()
#   item['marca'] = 'Adidas'
#   item['precio'] = response.xpath("//div[@class='productprice___2Mip5 gl-vspace']/div/div/div/div[1]/text()").get()
#   # item['color'] = response.xpath("//div[@class='sidebar-colorchooser___i7JXW']/div[@class='color-label___2hXaD']/text()").get()
#   item['url_raiz'] = self.link_raiz
#   item['url_calzado'] = response.url
#   # Elemento que contiene el json para obtener rating del  producto
#   json_element_rating=  response.xpath("/html/body/script[6]/text()").get().replace("window.DATA_STORE = JSON.parse",'')[2:-3]
#   # Decodificacion del json para el rating
#   json_element_rating=
#   json_element_rating.encode().decode('unicode-escape')
#   json_rating=json.loads(json_element_rating)
#   # Elemento que contiene el json para obtener tallas y  descripcion del producto
#   json_element =
#   response.xpath("//body/script[7]/text()").get().replace('window.REACT_Q
#   UERY_DATA = ','')
#   data_json=json.loads(json_element)
#   tallas = truco.find_jsonLabel(obj=data_json,etiqueta='size')
#   imagenes =
#   truco.find_jsonLabel(obj=data_json,etiqueta='image_url')
#   color = truco.find_jsonLabel(obj=data_json,etiqueta='color')[0]
#   # color =
#   truco.find_jsonLabel(obj=data_json,etiqueta='reviewCount')[0]
#   calificacion
#   = truco.find_jsonLabel(obj=json_rating,etiqueta="overallRating")
#   print('DATA JSON:')
#   print(calificacion)
#   # item['descripcion'] = response.xpath("//div[@class='textcontent___13aRm']/h3/text()").getall()
#   104
#   item['descripcion'] =
#   str(truco.find_jsonLabel(obj=data_json,etiqueta='subtitle')[0]).strip()
#   # print(f'Color calzado: {color}')
#   item['tallas'] = (truco.limpiar_lista(tallas))
#   item['imagenes'] = imagenes
#   item['color'] = color
#   if esNuevo:
#   item['calificacion'] = -1 if str(esNuevo).lower() == 'new'
#   else calificacion[0]
#   else:
#   if len(calificacion)>0:
#   item['calificacion'] = calificacion[0]
#   else:
#   item['calificacion'] = 0
#   print(item['calificacio'])
#   yield item
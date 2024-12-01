# store_config.py
store_config = {
    # "maxxicomp": {
    #   "allowed_domains":"maxxicomp.com",
    #   "start_urls": [
    #     "https://maxxicomp.com/7-laptops?q=Marca-HP"
    #   ],
    #   "product_card_xpath":"//div[@id='js-product-list']//div[@class='item']//div[@class='element-top']/a",
    #   "button_close_modal_xpath":"//div[@class='cp-popup-close-button']",
    #   "next_button_xpath":"//nav[@class='pagination']//a[contains(@class,'next')]",
    #   "title_xpath":"//h1[@class='product_title']/text()",
    #   "urlImg_xpath":"//div[contains(@class,'product-images-thumb')]//img/@data-src",
    #   "price_xpath":"//div[contains(@class,'product-price')]//span[contains(@class,'current-price')]/text()",
    #   "description_xpath":"//div[@id='description']//p/text()",
    #   "category_xpath":"//h1[@class='product_title']/text()",
    #   "brand_xpath":"//div[contains(@class,'product-manufacturer')]/a/text()",
    #   "stock_xpath":"//div[@id='product-availability']//span/text()",
    #   "availability_xpath":"////div[@id='product-availability']//span/text()"
    # },
    # "pclaptop":{
    #   "allowed_domains":"pclaptop.com.ec",
    #   "start_urls": [
    #       "https://pclaptop.com.ec/tienda/?wpf=wpf_65df5c5b9465c&wpf_cols=3&wpf_filtros=lenovo"
    #   ],
    #   "product_card_xpath":"//ul[contains(@class,'product')]/li//a[contains(@class,'LoopProduct-link')]",
    #   "button_close_modal_xpath":"",
    #   "next_button_xpath":"",
    #   "title_xpath":"//h3[contains(@class,'product_title')]/text()",
    #   "price_xpath":"//div[contains(@class,'woocommerce-product-price')]//span[contains(@class,'Price-amount')]/bdi/text()",
    #   "description_xpath":"//div[contains(@class,'product-content')]/div//li/text()",
    #   "urlImg_xpath":"//div[contains(@class,'product-gallery__image')]//img/@src",
    #  "category_xpath":"",
    #   "brand_xpath":"//span[@class='detail-content']/a/text()",
    #   "stock_xpath":"",
    #   "availability_xpath" : ""
    # },
    # "pinsoft":{
    #   "allowed_domains":"pinsoft.ec",
    #   "start_urls": [
    #     "https://www.pinsoft.ec/dell/c-71.html"
    #   ],
    #   "product_card_xpath":"//div[@id='r_spisok']//div[contains(@class,'product')]//a",
    #   "button_close_modal_xpath":"",
    #   "next_button_xpath":"",
    #   "title_xpath":"//h1[contains(@class,'category_heading')]/text()",
    #   "urlImg_xpath":"//div[@class='additional_images2']//a/@href",
    #   "price_xpath":"//span[contains(@class,'new_price_card_product')]/text()",
    #   "description_xpath":"//div[contains(@class,'product-content')]/div//li/text()",
    #   "category_xpath":"//ol[@class='breadcrumb']//a/span/text()",
    #   "brand_xpath":"//div[@id='tab-description']//tbody/tr[1]/td[2]/text()",
    #   "stock_xpath":"",
    #   "availability_xpath" : "//span[contains(@class,'label-stock')]/text()"
    # },
    # "tekboss":{
    #   "allowed_domains":"tekboss.com.ec",
    #   "start_urls": [
    #     'https://www.tekboss.com.ec/categoria-producto/laptops/hp/'
    #   ],
    #   "product_card_xpath":"//ul[contains(@class,'products')]/li//div[@data-link-url]//div[contains(@class,'product_title')]//a",
    #   "button_close_modal_xpath":"",
    #   "next_button_xpath":"",
    #   "title_xpath":"//div[contains(@class,'title')]//h1/text()",
    #   "urlImg_xpath":"//div[contains(@class,'woocommerce-product-gallery__wrapper')]//img/@src",
    #   "price_xpath":"//p[@class='price']/span[contains(@class,'price_extra')]/text()",
    #   "description_xpath":"//table[contains(@class,'product-attributes')]//tr/text()",
    #   "category_xpath":"//nav[@class='woocommerce-breadcrumb']//span[@class='breadcrumb-item'][2]/a/text()",
    #   "brand_xpath":"//nav[@class='woocommerce-breadcrumb']//span[@class='breadcrumb-item'][3]/a/text()",
    #   "stock_xpath":"",
    #   "availability_xpath" : ""
    # },
    # "planetadigital":{
    #   "allowed_domains":"planetadigitalec.com",
    #   "start_urls": [
    #     'https://planetadigitalec.com/collections/gaming-laptops/dell'
    #   ],
    #   "product_card_xpath":"//main[@id='MainContent']//div[contains(@class,'item')]//a",
    #   "button_close_modal_xpath":"",
    #   "next_button_xpath":"",
    #   "title_xpath":"//h1[contains(@class,'title')]/text()",
    #   "urlImg_xpath":"//div[@class='photos']//a/@href",
    #   "price_xpath":"//span[@id='ProductPrice-product-template']/text()",
    #   "description_xpath":"//div[contains(@class,'product-single')]/p",
    #   "category_xpath":"//div[contains(@class,'return-link')]/a/text()",
    #   "brand_xpath":"//h1[contains(@class,'title')]/text()",
    #   "stock_xpath":"",
    #   "availability_xpath" : ""
    # },
    # "mobilestore":{
    #   "allowed_domains":"mobilestore.ec",
    #   "start_urls": [
    #     'https://mobilestore.ec/categoria-producto/computadoras-mobile-store/lenovo/'
    #   ],
    #   "product_card_xpath":"//ul[contains(@class,'products')]/li//div[contains(@class,'image__wrapper')]/a[contains(@class,'Product-link')]",
    #   "button_close_modal_xpath":"",
    #   "next_button_xpath":"",
    #   "title_xpath":"//h1[contains(@class,'product_title')]/text()",
    #   "urlImg_xpath":"//div[contains(@class,'woocommerce-product-gallery')]//ol/li/img/@src",
    #   "price_xpath":"//p[@class='price']/span[contains(@class,'price_extra')]/text()",
    #   "description_xpath":"//div[@class='woocommerce-product-details__short-description']//ul/li/text()",
    #  "category_xpath":"",
    #   "brand_xpath":"//h1[contains(@class,'title')]/text()",
    #   "stock_xpath":"//div[contains(@class,'product-stock')]//p/text()",
    #   "availability_xpath" : "//div[contains(@class,'product-stock')]//p/text()"
    # },
    # "novicompu":{
    #    "allowed_domains":"novicompu.com",
    #   "start_urls": [
    #     'https://www.novicompu.com/computadoras/laptops/dell?initialMap=c,c&initialQuery=computadoras/laptops&map=category-1,category-2,brand'
    #   ],
    #   "product_card_xpath":"//section[contains(@class,'vtex-product-summary')]/a",
    #   "button_close_modal_xpath":"",
    #   "next_button_xpath":"//div[contains(@class,'buttonShowMore')]//div[contains(@class,'vtex-button__label')]",
    #   "title_xpath":"//div[contains(@class,'product-main')]//span[contains(@class,'productBrand--product')]/text()",
    #   "urlImg_xpath":"//div[contains(@class,'productImagesContainer')]//div[contains(@class,'productImagesThumb')]//img/@src",
    #   "price_xpath":"//div[contains(@class,'product-main')]//div[contains(@class,'items-stretch')]//span[contains(@class,'product-price-1-x-currencyContainer')]//span/text()",
    #   "description_xpath":"//div[contains(@class,'product-main')]//div[contains(@class,'productDescriptionText')]/div/text()",
    #   "category_xpath":"//div[@data-testid='breadcrumb']//span[2]/a/text()",
    #   "brand_xpath":"//div[contains(@class,'product-main')]//span[contains(@class,'productBrand--product')]/text()",
    #   "stock_xpath":"//div[contains(@class,'product-availability')]//span/text()",
    #   "availability_xpath" : "//div[contains(@class,'product-availability')]//span/text()"
    # },
    #   "superpaco":{
    #    "allowed_domains":"superpaco.com",
    #   "start_urls": [
    #     'https://www.superpaco.com/tecnologia/computadores-y-accesorios/portatiles/asus?initialMap=c,c,c&initialQuery=tecnologia/computadores-y-accesorios/portatiles&map=category-1,category-2,category-3,brand'
    #   ],
    #   "product_card_xpath":"//div[@id='gallery-layout-container']//section/a",
    #   "button_close_modal_xpath":"",
    #   "next_button_xpath":"",
    #   "title_xpath":"//h1[contains(@class,'productNameContainer')]//span/text()",
    #   "urlImg_xpath":"//div[contains(@class,'infoImage')]//img/@src",
    #   "price_xpath":"//div[@id='contentPrice']",
    #   "description_xpath":"//div[contains(@class,'product-short-description')]/text()",
    #   "category_xpath":"//div[contains(@class,'Breadcrumb')]//div[@data-testid='breadcrumb']//span[3]/a/text()",
    #   "brand_xpath":"(//div[contains(@class,'productBrandContainer')]//span/text())[1]",
    #   "stock_xpath":"",
    #   "availability_xpath" : "//div[contains(@class,'product-availability')]//span/text()"
    #   # //div[contains(@class,'productSpecificationGroup')]/span[contains(@data-specification-group,'Especificaciones')]/text()
    # },
    #   "tecnogame":{
    #    "allowed_domains":"tecnogame.ec",
    #   "start_urls": [
    #     'https://tecnogame.ec/venta-de/laptops-en-guayaquil-notebooks-accesorios/?filter_marca=dell'
    #   ],
    #   "product_card_xpath":"//ul[contains(@class,'products')]//div[@class='woocommerce-image__wrapper']/a",
    #   "button_close_modal_xpath":"",
    #   "next_button_xpath":"",
    #   "title_xpath":"//h1[contains(@class,'entry-title')]/text()",
    #   "urlImg_xpath":"//ul[contains(@class,'gallery')]/li//img/@src",
    #   "price_xpath":"//p[@class='price']//bdi/text()",
    #   "description_xpath":"//div[contains(@class,'product-details')]/ul/li/text()",
    #   "category_xpath":"//div[@class='product_meta']//span[@class='posted_in']/a/text()",
    #   "brand_xpath":"//table[contains(@class, 'woocommerce-product-attributes')]//tr[th[text()='Marca']]//td//text()",
    #   "stock_xpath":"",
    #   "availability_xpath" : "//p[contains(@class,'in-stock')]/text()"
    #   # //div[contains(@class,'productSpecificationGroup')]/span[contains(@data-specification-group,'Especificaciones')]/text()
    # },
      "tecnomegastore":{
       "allowed_domains":"tecnomegastore.ec",
      "start_urls": [
        'https://tecnomegastore.ec/category/1/3N003-pc-laptop-portatil-notebook'
      ],
      "product_card_xpath":"//div[contains(@class,'container-tm')]//a",
      "button_close_modal_xpath":"",
      "next_button_xpath":"",
      "title_xpath":"//h1[contains(@class,'entry-title')]/text()",
      "urlImg_xpath":"//ul[contains(@class,'gallery')]/li//img/@src",
      "price_xpath":"//p[@class='price']//bdi/text()",
      "description_xpath":"//div[contains(@class,'product-details')]/ul/li/text()",
      "category_xpath":"//div[@class='product_meta']//span[@class='posted_in']/a/text()",
      "brand_xpath":"//table[contains(@class, 'woocommerce-product-attributes')]//tr[th[text()='Marca']]//td//text()",
      "stock_xpath":"",
      "availability_xpath" : "//p[contains(@class,'in-stock')]/text()"
      # //div[contains(@class,'productSpecificationGroup')]/span[contains(@data-specification-group,'Especificaciones')]/text()
    },
        "artefacta":{
       "allowed_domains":"artefacta.com",
      "start_urls": [
        'https://www.artefacta.com/c/tecnologia/computacion/laptops?marca=43403'
      ],
      "product_card_xpath":"//ol[contains(@class,'products')]/li//a[contains(@class,'product-item-photo')]",
      "button_close_modal_xpath":"",
      "next_button_xpath":"//div[contains(@class,'buttonShowMore')]//div[contains(@class,'vtex-button__label')]",
      "title_xpath":"//h1[@class='page-title']/span/text()",
      "urlImg_xpath":"//div[contains(@class, 'fotorama-item')]//img/@src",
      "price_xpath":"//div[contains(@class,'product-info-price')]//span[@data-price-type='finalPrice']//span/text()",
      "description_xpath":"//table[@id='product-attribute-specs-table']//tr",
      "category_xpath":"//h1[@class='page-title']/span/text()",
      "brand_xpath":"//table[@id='product-attribute-specs-table']//tr//td[@data-th='Marca']/text()",
      "stock_xpath":"",
      "availability_xpath" : "//p[contains(@class,'in-stock')]/text()"
      # //div[contains(@class,'productSpecificationGroup')]/span[contains(@data-specification-group,'Especificaciones')]/text()
    },
      
}

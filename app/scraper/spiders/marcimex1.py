from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class MarcimexSpiderSelenium:
    def __init__(self):
        # Configuración de Selenium y el navegador
        chrome_options = webdriver.ChromeOptions()
        prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "translate_whitelists": {"en": "es"},
            "translate": {"enabled": "true"}
        }
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--lang=es")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.maximize_window()

    def scrape(self):
        self.driver.get('https://www.marcimex.com/tecnologia')

        # Esperar hasta que todos los productos estén cargados
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@id="gallery-layout-container"]'))
        )

        url_array = []
        while True:
            try:
                # Cerrar el modal si aparece
                close_button = self.driver.find_element(By.XPATH, '//div[@class="kevin"]')
                close_button.click()
            except:
                pass

            # Obtén las URLs de los productos
            link_elements = self.driver.find_elements(By.XPATH, '//div[@id="gallery-layout-container"]//section[contains(@class,"vtex-product-summary")]/a')
            for link in link_elements:
                href = link.get_attribute('href')
                if href:
                    url_array.append(href)

            try:
                # Hacer clic en el botón de siguiente página
                boton_avanzar = self.driver.find_element(By.XPATH, '//div[contains(@class,"vtex-search-result-3-x-buttonShowMore")]/a')
                boton_avanzar.click()

                # Esperar que cargue la nueva página completamente
                WebDriverWait(self.driver, 10).until(EC.staleness_of(boton_avanzar))

            except:
                print("No hay más páginas. Saliendo del bucle.")
                break

        # Scrapeando cada producto individualmente
        for url in url_array:
            print("PRODUCTO : ", url)
            self.scrape_product(url)

        self.driver.quit()

    def scrape_product(self, url):
        # Ir a la página del producto
        self.driver.get(url)

        try:
            # Esperar hasta que el título esté presente
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"Content--producto-info")]//div[contains(@class,"flexRow--nombre-prpducto")]//h1[contains(@class,"vtex-store-components-3-x-productNameContainer")]'))
            )

            # Extraer el título
            title = self.driver.find_element(By.XPATH, '//div[contains(@class,"Content--producto-info")]//div[contains(@class,"flexRow--nombre-prpducto")]//h1[contains(@class,"productNameContainer")]').text
            print("TITLE: ", title)

            # Extraer la descripción
            # description = self.driver.find_element(By.XPATH, "//div[contains(@class,'content--description-pdp')]/div").text
            # print("DESCRIPTION: ", description)

        except Exception as e:
            print("Error al scrapear el producto:", str(e))
            pass

# Ejecutar el scraper
if __name__ == "__main__":
    spider = MarcimexSpiderSelenium()
    spider.scrape()

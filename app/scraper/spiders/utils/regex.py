import re

class Regex:
  
  PRICE = r"\s?(\d{1,3}(?:[\.,]\d{3})*[\.,]\d{2})"
  SISTEMA_OPERATIVO = r"(Windows|Microsoft Windows|Free DOS|Linux|Ubuntu)\s*(\d+)?\s*(Home|Pro|Professional)?"
  
  PROCESADOR_I_1 = r'(?:[Ii]ntel(?:\s*®)?)?\s*[Cc]ore(?:\s*™)?\s*i\d+(?:[-\w]*)?\s*(\d+(\.\d+)?\s*GHz)?'
  PROCESADOR_I_2= r"/[Ii]ntel\s*[Cc]ore\s*i\d+[-\w]*\s*(\d+(\.\d+)?\s*GHz)?"
  PROCESADOR_R_1=r"(?:[Aa][Mm][Dd]\s*)?[Rr]yzen\s*\d+\s*[-\w]*"
  PROCESADOR_R_2=r"(?:[Aa][Mm][Dd](?:\s*®)?)?\s*[Rr]yzen(?:\s*™)?\s*\d+\s*[-\w]*"
  PROCESADOR_I_TITLE_1 =r'(?:[Ii]ntel(?:\s*®)?)?\s*[Cc]ore(?:\s*™)?\s*i\d+(?:[-\w]*)?\s*(\d+(\.\d+)?\s*GHz)?'
  PROCESADOR_I_TITLE_2=r"/[Ii]ntel\s*[Cc]ore\s*i\d+[-\w]*\s*(\d+(\.\d+)?\s*GHz)?"
  PROCESADOR_R_TITLE_1=r"(?:[Aa][Mm][Dd]\s*)?[Rr]yzen\s*\d+\s*[-\w]*"
  PROCESADOR_R_TITLE_2=r"(?:[Aa][Mm][Dd](?:\s*®)?)?\s*[Rr]yzen(?:\s*™)?\s*\d+\s*[-\w]*"
  ALMACENAMIENTO_1=r"(\d+(?:\.\d+)?\s*([Gg][Bb]|[Tt][Bb]))\s*(HDD|SSD|PCIe|NVMe|SATA|Disco\s*duro|Unidad\s*de\s*estado\s*líquido)?"
  ALMACENAMIENTO_2=r"(\d+(?:\.\d+)?\s*(G[Bb]|[Tt][Bb]))\s*(HDD|SSD|PCIe|NVMe|SATA|Disco\s*duro|Unidad\s*de\s*estado\s*líquido)?"
  PANTALLA_TAMAÑO_1=r'''\b(1[0-9](?:[.,]\d+)?|[2-9][0-9](?:[.,]\d+)?)\s*(?:pulgadas|[Pp][Uu][Ll][Gg]|["«”’']{1,2})'''
  PANTALLA_TAMAÑO_2=r'''(1[0-9](?:[.,]\d+)?|[2-9][0-9](?:[.,]\d+)?)\s*(?:pulgadas|[Pp][Uu][Ll][Gg]|["«”'″]{1,2})'''
  PANTALLA_TAMAÑO_3=r'''\b(1[0-9](?:[.,]\d+)?|[2-9][0-9](?:[.,]\d+)?)\s*(?:pulgadas|[Pp][Uu][Ll][Gg]|["«”’']{1,2})'''
  
  CATEGORY_1=r"(Laptop(s)?|Computador(as)?|Tablet(s)?|Celular(es)?|Notebook(s)?|Accesorios de PC|Monitor(es)?|Impresora(s)?|Smartwatch(es)?|Cámar(as)? Digital(es)?|Teclado(s)?|Mouse(s)?|Bateria(s)?)|Portátil(es)?"
  
  BRAND_1 = r"(Lenovo|HP|Acer|Asus|Dell|Samsung|Huawei|Vostro|MSI)"
  
  STOCK_1 = r"\b\d+(\.\d+)?\b"

  @staticmethod
  def extract_precio(text):
    match = re.search(Regex.PRICE, text, re.IGNORECASE)
    if match:
      return match.group(1).replace(',', '.')
    return -1
  
  @staticmethod
  def extract_sistema_operativo(description, title):
    match = re.search(Regex.SISTEMA_OPERATIVO, description, re.IGNORECASE)
    return match.group(0).strip() if match else None

  @staticmethod
  def  extract_procesador(description, title):
    #Intel® Core™ i5-1135G7
    match2 = re.search(Regex.PROCESADOR_I_1, description, re.IGNORECASE)
    print("MATCH 2 Procesador :  ", match2)
    if match2:
      return match2.group(0).strip()
    #Intel Core i3-1115G4
    match1 = re.search(Regex.PROCESADOR_I_2, description, re.IGNORECASE)
    print("MATCH 1 Procesador :  ", match1)
    if match1:
      return match1.group(0).strip()

    #AMD Ryzen 5 3500U
    match3 = re.search(Regex.PROCESADOR_R_1, description, re.IGNORECASE)
    if match3:
      return match3.group(0).strip()
    # AMD Ryzen ™ 7 3700U
    match4 = re.search(Regex.PROCESADOR_R_2, description, re.IGNORECASE)
    if match4:
      return match4.group(0).strip()
    
    #TITULO
    #Intel® Core™ i5-1135G7
    match5 = re.search(Regex.PROCESADOR_I_TITLE_1, title, re.IGNORECASE)
    if match5:
      return match5.group(0).strip()
    #Intel Core i3-1115G4
    match6 = re.search(Regex.PROCESADOR_I_TITLE_2, title, re.IGNORECASE)
    print("MATCH 1 Procesador :  ", match6)
    if match6:
      return match6.group(0).strip()

    #AMD Ryzen 5 3500U
    match7 = re.search(Regex.PROCESADOR_R_TITLE_1, title, re.IGNORECASE)
    if match7:
      return match7.group(0).strip()
    # AMD Ryzen ™ 7 3700U
    match8 = re.search(Regex.PROCESADOR_R_TITLE_2, title, re.IGNORECASE)
    if match8:
      return match8.group(0).strip()
    return "Otra"
  
  @staticmethod
  def extract_ram(description, title):
    # Extrae solo el tamaño en GB para RAM dentro del rango de 1-32 GB
    match_1 = re.search(r"Memoria\s*[Rr][Aa][Mm][:\s]*.*?(\d+\s*[Gg][Bb])", description, re.IGNORECASE)
    if match_1:
      return match_1.group(1).strip()
    #(?:Memoria\s*RAM:.*)(\d+\d+\s*GB)
    match_2 = re.search(r"(\d+\s*(gb|GB))\s*(ram|RAM)", description, re.IGNORECASE)
    if match_2:
      return match_2.group(1).strip()
    
    match_3 = re.search(r"(?:Memoria\s*RAM:.*)?(\d+\s*GB)(?:.*RAM)?", description, re.IGNORECASE)
    if match_3:
      return match_3.group(1).strip()
    return "Otra"
  
  @staticmethod
  def extract_almacenamiento(description, title):
    match = re.search(Regex.ALMACENAMIENTO_1, description, re.IGNORECASE)
    if match:
        size = match.group(1).strip()  # El valor numérico y la unidad (GB o TB)
        storage_type = match.group(3) if match.group(3) else ""  # El tipo de almacenamiento (HDD, SSD, etc.)
        return f"{size} {storage_type}".strip()
    
    matchTitle=re.search(Regex.ALMACENAMIENTO_2, title, re.IGNORECASE)
    if matchTitle:
      size = match.group(1).strip()  # El valor numérico y la unidad (GB o TB)
      storage_type = match.group(3) if match.group(3) else ""  # El tipo de almacenamiento (HDD, SSD, etc.)
      return f"{size} {storage_type}".strip()
    return "Otra"

  
  @staticmethod
  def extract_tamaño_pantalla(description, title):
    match = re.search(Regex.PANTALLA_TAMAÑO_1, description, re.IGNORECASE)
    if match:
      return match.group(0) 
    
    match2 = re.search(Regex.PANTALLA_TAMAÑO_2,description,re.IGNORECASE)
    if match2:
      return match2.group(0)
    
    matchTitle = re.search(Regex.PANTALLA_TAMAÑO_3, title, re.IGNORECASE)
    if matchTitle:
      return matchTitle.group(0)
    
    return "Otra"
  
  @staticmethod
  def extract_graficos(description, title):
    match = re.search(r"(Intel UHD|Intel Iris Xe|AMD Radeon|NVIDIA GTX|Gráficos integrados| vega\s\d |  Graphics UHD)", description, re.IGNORECASE)   
    if match:
      return match.group(0) 
    matchTitle = re.search(r"(Intel UHD|Intel Iris Xe|AMD Radeon|NVIDIA GTX|Gráficos integrados| vega\s\d)", title, re.IGNORECASE)
    if matchTitle:
      return matchTitle.group(0)
    return "Otra"
  
  # @staticmethod
  # def extract_tipo_pantall(text):
  #   return None;
  
  @staticmethod
  def extract_teclado(text):
    return None
  
  @staticmethod
  def extract_audio(text):
    return None
  
  @staticmethod
  def extract_wifi(text):
    # Regex para obtener el wifi:
    match_wifi_1 = re.search(r"(Wi-Fi\s*[6E]|\b802\.11[a-z]+(?:\[a-z]+)?)", text, re.IGNORECASE)
    if(match_wifi_1):
      return match_wifi_1[0]
    return "Wifi"

  @staticmethod
  def extract_bluetooth(text):
    match_bluetooth_1 = re.search( r"Bluetooth(?:[:®]?\s*\d+(?:\.\d+)?|\b)", text, re.IGNORECASE)
    if match_bluetooth_1:
      return match_bluetooth_1
    return ""
  
  @staticmethod
  def extract_puertos(text):
    return None
  
  @staticmethod
  def extract_category(text):
    match =re.search(Regex.CATEGORY_1,text,re.IGNORECASE)
    if match:
      return match.group(0)
    return "Otra"

  @staticmethod
  def extract_brand(text):
    match = re.search(Regex.BRAND_1, text, re.IGNORECASE)
    if match:
      return match.group(0)
    return "Otra"
    
  @staticmethod
  def extract_stock(text):
        text = text.strip()  # Elimina espacios en blanco al inicio y al final
        match = re.search(Regex.STOCK_1, text, re.IGNORECASE)
        if match:
            print(f"MATCH STOCK: {match.group()}")  # Captura el número completo
            return float(match.group()) if '.' in match.group() else int(match.group())
        print("No se encontró stock.")
        return -1  # Si no hay coincidencia, devuelve -1
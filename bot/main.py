import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def leer_lineas(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
    return [linea.strip() for linea in lineas if linea.strip()]

def enviar_lineas(driver, grupo, lineas, espera_entre_lineas=2):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    import time

    buscador = driver.find_element(By.XPATH, '//div[@title="Buscar o empezar un chat nuevo"]')
    buscador.click()
    time.sleep(1)
    buscador.send_keys(grupo)
    time.sleep(2)
    buscador.send_keys(Keys.ENTER)
    time.sleep(2)

    caja = driver.find_element(By.XPATH, '//div[@title="Escribe un mensaje aquí"]')

    for linea in lineas:
        caja.send_keys(linea)
        caja.send_keys(Keys.ENTER)
        time.sleep(espera_entre_lineas)

if __name__ == "__main__":
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sesion_path = os.path.join(root_dir, "sesion_whatsapp")
    ruta_mensaje = os.path.join(root_dir, "mensaje.txt")

    if not os.path.exists(sesion_path):
        os.makedirs(sesion_path)

    opciones = Options()
    opciones.add_argument(f"user-data-dir={sesion_path}")

    driver = webdriver.Chrome(options=opciones)
    driver.get("https://web.whatsapp.com")
    time.sleep(15)

    grupo = "Salvando vidas apoyo Casa del Rey 2025"
    lineas = leer_lineas(ruta_mensaje)
    enviar_lineas(driver, grupo, lineas)

    print("Mensajes enviados línea por línea.")

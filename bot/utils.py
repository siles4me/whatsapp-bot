def leer_y_dividir_texto(ruta_archivo, tamano_bloque=500):
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
    return [texto[i:i+tamano_bloque] for i in range(0, len(texto), tamano_bloque)]

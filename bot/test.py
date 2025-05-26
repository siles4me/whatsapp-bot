

import os
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ruta_mensaje = os.path.join(root_dir, "mensaje.txt")
print("Ruta absoluta archivo:", ruta_mensaje)
print("¿Existe archivo?", os.path.exists(ruta_mensaje))

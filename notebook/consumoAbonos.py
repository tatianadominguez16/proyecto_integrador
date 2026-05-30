import requests

def consumir_facturas_tabla_abonos():

    url="http://localhost:8080/api/abonos"

    respuesta=requests.get(url)

    respuesta.raise_for_status()

    datos=respuesta.json()

    return datos
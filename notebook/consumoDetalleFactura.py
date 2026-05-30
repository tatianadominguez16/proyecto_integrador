import requests
def consumir_facturas_tabla_detalle_factura():

    url="http://localhost:8080/api/detalle-facturas"

    respuesta=requests.get(url)

    respuesta.raise_for_status()

    datos=respuesta.json()

    return datos
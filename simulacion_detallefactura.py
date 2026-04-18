import random

from datetime import datetime,timedelta

def generar_simulacion(numeroSimulaciones):

    articulos=["Jeans,camisas,vestidos,faldas"]
    id_consecutivos=["23","21","34","45"]
    

    detallefactura=[]
    for _ in range(numerodetallefactura):

        simulacion={
            "id_consecutivo":random.choice(id_consecutivos),
            "factura":random.choice(facturas),
            "cantidad":random.choice(cantidades),
            "articulo":random.choice(articulos),
            "valor_venta" :random.randint(10000,500000),
        }

        #inyectando errores controlados
        probabilidadError = random.random()
        if probabilidadError<0.1:
            simulacion["id_consecutivo"]=random.choice([None, -1,0])
            simulacion["cantidad"]=" "+simulacion["cantidad"]+" "
        elif probabilidadError<0.25:
            simulacion["valor_venta"]=None
        elif probabilidadError<0.4:
            simulacion["codigo"]=simulacion["codigo"].lower()
            simulacion["valor_venta"]=random.choice([-1000,0,200])
            simulacion["id_consecutivo"]=None
        elif probabilidadError<0.7:
            simulacion["valor_venta"]=0
        elif probabilidadError<0.9:
            simulacion["articulo"]=random.choice(["Papitas montañeras","gaseosa doble"])

        detallefactura.append(simulacion)
    return detallefactura
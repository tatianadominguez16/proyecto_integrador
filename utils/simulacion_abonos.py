from datetime import datetime,timedelta
import random
def simulador_abonos(numeroAbonos):
    #semilla de datos 
    listaNombreClientes=["juan","Andres","Maria","Carlos",
    "Andrea","Esteban"]
    listaDeCodigos=["A01","A02","A03","A04","A05","A06 "]
    fechaInicial=datetime(2023,1,1)

    abonos=[]

    for _ in range(numeroAbonos):
        fechaSimilada=fechaInicial+timedelta(days=random.randint(0,365))
        abono={
            "id_abonos":random.randint(0,50000),
            "cliente":random.choice(listaNombreClientes),
            "factura":random.choice(listaDeCodigos),
            "valorabonado":random.randint(10000,500000),
            "valorestante":random.randint(10000,500000),
            "fecha":fechaSimilada.strftime("%Y-%m-%d"),
            "valor deuda":random.randint(10000,500000)

        }

        #inyectando errores controlados
        probabilidadError=random.random()
        if probabilidadError<0.1:
            abono["valorabonado"]=None
        elif probabilidadError<0.2:
            abono["fecha"]=None
        elif probabilidadError<0.3:
            abono["cliente"]=""
        elif probabilidadError<0.4:
            abono["valorabonado"]= -5000
        elif probabilidadError<0.5:
            abono["valorabonado"]= "cincuenta mil"


        abonos.append(abono)
    return abonos

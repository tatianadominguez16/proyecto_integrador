from datetime import datetime,timedelta
import random
def simulador_abonos(numeroAbonnos):
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
            "cliente":random.chice(listaNombreClientes),
            "factura":random.choice(listaDeCodigos),
            "valor abonado":random.randint(10000,500000),
            "valor restante":random.randint(10000,500000),
            "fecha":fechaSimilada.strftime("%Y-%m-%d"),
            "valor deuda":random.randint(10000,500000)

        }
        abonos.append(abono)
    return abonos

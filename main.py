import pandas as pd


#zona para importar simulaciones
from utils.simulacion_abonos import simulador_abonos
from utils.simulacion_detallefactura import generar_simulacion

#zona para importar limpiezas
from notebook.limpieza import limpiar_simulacion
from notebook.limpieza_detalle_factura import limpiar_detalle_factura

#zona para importar descripciones
from notebook.descripcion_abonos import describir_simulacion
from notebook.descripcion import describir_datos


abonos=simulador_abonos(100)
abonos_ordenados=pd.DataFrame(abonos)
abonos_limpios=limpiar_simulacion(abonos_ordenados)
describir_simulacion(abonos_limpios)

detalle_factura=generar_simulacion(100)
detalle_factura_ordenado=pd.DataFrame(detalle_factura)
detalle_factura_limpio=limpiar_detalle_factura(detalle_factura_ordenado)
describir_datos(detalle_factura_limpio) 
import pandas as pd

from notebook.limpieza import limpiar_simulacion

from utils.simulacion_abonos import simulador_abonos

abonos=simulador_abonos(100)
abonos_ordenados=pd.DataFrame(abonos)
abonos_limpios=limpiar_simulacion(abonos_ordenados)
print(abonos_limpios)
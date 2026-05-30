import pandas as pd

def transformar_abonos(data_frame_limpio):

    filtro=data_frame_limpio.query("valordeuda==400000") 
    agrupacion=filtro.groupby("fecha")["id_abonos"].count().reset_index(name="conteo")

    filtro2=data_frame_limpio.query("valorabonado>=200000")
    agrupacion2=filtro2.groupby("fecha")["id_abonos"].sum().reset_index(name="sumatoria")

    transformacion_resumen={
        "conteovalordeuda":agrupacion,
        "sumatoriavalorabonado":agrupacion2
    }

    return transformacion_resumen
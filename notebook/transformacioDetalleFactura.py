import pandas as pd

def transformar_datos(data_frame_limpio):

    filtro=data_frame_limpio.query("articulo== 'Jeans' ")
    agrupacion=filtro.groupby("cantidad")["id_consecutivo"].count().reset_index(name="conteo")

    filtro2=data_frame_limpio.query("cantidad>=10")
    agrupacion2=filtro2.groupby("articulo")["cantidad"].sum().reset_index(name="sumatoria")

    transformacion_resumen={
        "conteoJeansPorValorVenta":agrupacion,
        "sumatoriaCamisasJeans":agrupacion2
    }

    return transformacion_resumen




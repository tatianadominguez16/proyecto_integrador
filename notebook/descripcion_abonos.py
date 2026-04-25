import pandas as pd

def describir_simulacion(data_frame_limpio):
    print(f"numero de filas: {data_frame_limpio.shape[0]}")
    print(f"numero de columnas: {data_frame_limpio.shape[1]}")
    print(f"columnas disponibles: {list(data_frame_limpio.columns)}")
    print(f"estadísticas: {data_frame_limpio[['id_abonos', 'valorabonado', 'valordeuda','valorrestante']].describe()}")
    print(f"valores categóricos: {data_frame_limpio['factura'].value_counts()}")
    print(f"fecha mínima: {data_frame_limpio['fecha'].min()}")
    print(f"fecha máxima: {data_frame_limpio['fecha'].max()}")
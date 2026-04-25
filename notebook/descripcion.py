import pandas as pd

def describir_datos(data_frame_limpio):
    print(f"numero de filas {data_frame_limpio.shape[0]}")
    print(f"numero de columnas {data_frame_limpio.shape[1]}")
    print(f"columnas disponibles {list(data_frame_limpio.columns)}")
    print(f"estadisticas {data_frame_limpio[['id_consecutivo','valor_venta']].describe()}")
    print(f"valores categoricos {data_frame_limpio['articulo'].value_counts()}")
    
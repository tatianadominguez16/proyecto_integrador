import pandas as pd

def limpiar_simulacion(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()
    #1.limpiar las columnas del dataframe que son palabras string
    columnas_texto=["cliente""factura"]
    for columna in columnas_texto:
        data_frame_limpio[columna]=data_frame_limpio[columna].astype("string").str.strip()
    
      #2 definir valores esperados
    valores_validos = ["juan", "Andres", "Maria", "Carlos"]
    data_frame_limpio["cliente"] = data_frame_limpio["cliente"].where(
        data_frame_limpio["cliente"].isin(valores_validos), pd.NA)

    #3 Evaluar columnas numericas 
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"])
    data_frame_limpio["costo"] = pd.to_numeric(data_frame_limpio["costo"])

    #4 evaluar columnas de fecha
    data_frame_limpio["fecha"] = pd.to_datetime(data_frame_limpio["fecha"])

    #5 Reemplazar fechas nulas con una fecha por default 
    fecha_default = pd.to_datetime("2026-01-01")
    data_frame_limpio["fecha"] = data_frame_limpio["fecha"].fillna(fecha_default)

    #6 Eliminar registros nulos de campos obligatorios
    columnas_obligatorias = ["id", "cliente", "costo", "factura"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    #7 eliminar valores invalidos a nivel numerico 
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["costo"] >= 100000]

    #8 Eliminar registros duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio

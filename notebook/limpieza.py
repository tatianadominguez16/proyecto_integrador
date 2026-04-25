import pandas as pd

def limpiar_simulacion(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()
    
    # 1. Limpiar las columnas del dataframe que son palabras string
    columnas_texto = ["cliente", "factura"]  # Fixed: added comma
    for columna in columnas_texto:
        if columna in data_frame_limpio.columns:  # Check if column exists
            data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip()
    
    # 2. Definir valores esperados
    valores_validos = ["juan", "Andres", "Maria", "Carlos"]
    if "cliente" in data_frame_limpio.columns:
        data_frame_limpio["cliente"] = data_frame_limpio["cliente"].where(
            data_frame_limpio["cliente"].isin(valores_validos), pd.NA)

    # 3. Evaluar columnas numericas 
    if "id_abonos" in data_frame_limpio.columns:  # Fixed: was "id"
        data_frame_limpio["id_abonos"] = pd.to_numeric(data_frame_limpio["id_abonos"], errors='coerce')
    if "valorabonado" in data_frame_limpio.columns:  # Fixed: was "costo", assuming this is the cost column
        data_frame_limpio["valorabonado"] = pd.to_numeric(data_frame_limpio["valorabonado"], errors='coerce')

    # 4. Evaluar columnas de fecha
    if "fecha" in data_frame_limpio.columns:
        data_frame_limpio["fecha"] = pd.to_datetime(data_frame_limpio["fecha"], errors='coerce')

    # 5. Reemplazar fechas nulas con una fecha por default 
    fecha_default = pd.to_datetime("2026-01-01")
    if "fecha" in data_frame_limpio.columns:
        data_frame_limpio["fecha"] = data_frame_limpio["fecha"].fillna(fecha_default)

    # 6. Eliminar registros nulos de campos obligatorios
    columnas_obligatorias = ["id_abonos", "cliente", "valorabonado", "factura"]  # Fixed: updated names
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    # 7. Eliminar valores invalidos a nivel numerico 
    if "id_abonos" in data_frame_limpio.columns:
        data_frame_limpio = data_frame_limpio[data_frame_limpio["id_abonos"] > 0]
    if "valorabonado" in data_frame_limpio.columns:
        data_frame_limpio = data_frame_limpio[data_frame_limpio["valorabonado"] >= 100000]

    # 8. Eliminar registros duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio
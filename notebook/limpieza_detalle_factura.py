import pandas as pd

def limpiar_detalle_factura(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

    #1. Limpiar las columnas del dataframe que son palabras (strings)
    columnas_texto=["articulo"]
    for columna in columnas_texto:

        data_frame_limpio[columna] = data_frame_limpio[columna].str.strip()

    #2. Definir valores esperados
    articulos_validos=["Jeans","camisas","vestidos","faldas"]    
    data_frame_limpio["articulo"]=data_frame_limpio["articulo"].where(data_frame_limpio
    ["articulo"].isin(articulos_validos),pd.NA)

    #3. Evaluar columnas numericas
    data_frame_limpio["id_consecutivo"]=pd.to_numeric(data_frame_limpio["id_consecutivo"])
    data_frame_limpio["cantidad"]=pd.to_numeric(data_frame_limpio["cantidad"])
    data_frame_limpio["valor_venta"]=pd.to_numeric(data_frame_limpio["valor_venta"])

    
    #6. Eliminar registros nulos de campos obligatorios
    columnas_obligatorias=["id_consecutivo","articulo","cantidad"]
    data_frame_limpio = data_frame_limpio.fillna({
    "articulo": "Desconocido"
})
    

    #7. Eliminar valores invalidos a nivel numerico 
    data_frame_limpio=data_frame_limpio[data_frame_limpio["id_consecutivo"]>0]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["cantidad"]>=0]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["valor_venta"]>=0]

    #8. Eliminar valores duplicados
    data_frame_limpio=data_frame_limpio.drop_duplicates()

    return data_frame_limpio

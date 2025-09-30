import pandas as pd
import numpy as np

# conxion con el dataset
try:
    df = pd.read_csv('youtube-top-100-songs-2025.csv')
    print("Dataset cargado exitosamente.")
except FileNotFoundError:
    print("Error: El archivo CSV no se encontró. Asegúrate de que el nombre y la ruta sean correctos.")
    exit() # Termina la ejecución si no se encuentra el archivo

# ----------------------------------------------------------------------
## Paso 1: Mostrar las columnas del dataset
COLUMNA_ANALISIS = 'view_count' 
print(f"\nColumna seleccionada para análisis (Pasos 5 y 6): '{COLUMNA_ANALISIS}'")
# ----------------------------------------------------------------------

## Paso 2: Usar describe() para resumir la información del dataset

print("\n## 2. Resumen Estadístico del Dataset (describe())")
resumen_estadistico = df.describe()
print(resumen_estadistico)

# ----------------------------------------------------------------------

## Paso 3: Identificar los tipos de datos de cada columna (dtypes)

print("\n## 3. Tipos de Datos por Columna (dtypes)")
tipos_de_datos = df.dtypes
print(tipos_de_datos)

# --- Análisis sobre los tipos de datos ---
print("\nAnálisis del Paso 3:")
for columna, dtype in tipos_de_datos.items():
    # Uso de la sintaxis 'in' para simplificar la identificación de tipos
    if pd.api.types.is_numeric_dtype(dtype):
        print(f"- '{columna}': {dtype} -> Se pueden calcular **Medidas de Tendencia Central** (media, mediana), **Dispersión** (desviación estándar), y realizar **Correlaciones** o **Regresiones**.")
    elif pd.api.types.is_object_dtype(dtype):
        print(f"- '{columna}': {dtype} -> Se pueden realizar **Conteo de Frecuencias** (value_counts), **Agrupaciones** (groupby) y análisis de **texto** o **categorías**.")
    else:
        print(f"- '{columna}': {dtype} -> (Otro tipo) Se puede requerir una **conversión** para un análisis específico (ej. fechas).")

# ----------------------------------------------------------------------

## Paso 4: Mostrar los primeros y últimos registros (head(), tail())

print("\n## 4. Primeros y Últimos Registros")
print("\nPrimeros 5 Registros (head()):")
print(df.head())

print("\nÚltimos 5 Registros (tail()):")
print(df.tail())

# ----------------------------------------------------------------------

## Paso 5: Ordenar los resultados (sort_values())

print(f"\n## 5. Ordenamiento Ascendente por '{COLUMNA_ANALISIS}' (Menos Populares)")
# Ordenar de forma ascendente (menor a mayor)
df_ordenado_asc = df.sort_values(by=COLUMNA_ANALISIS, ascending=True)
print(df_ordenado_asc.head(5))

print(f"\nOrdenamiento Descendente por '{COLUMNA_ANALISIS}' (Más Populares)")
# Ordenar de forma descendente (mayor a menor)
df_ordenado_desc = df.sort_values(by=COLUMNA_ANALISIS, ascending=False)
print(df_ordenado_desc.head(5))

# ----------------------------------------------------------------------

## Paso 6: Cálculo de Medidas Estadísticas

print(f"\n## 6. Cálculo de Medidas Estadísticas para '{COLUMNA_ANALISIS}'")

# Se verifica que la columna seleccionada sea numérica.
if pd.api.types.is_numeric_dtype(df[COLUMNA_ANALISIS]):
    
    # a. Media (np.mean())
    media = np.mean(df[COLUMNA_ANALISIS])
    print(f"a. Media (Promedio de {COLUMNA_ANALISIS}): {media:,.0f}") # Formato con separador de miles

    # b. Mediana (np.median())
    mediana = np.median(df[COLUMNA_ANALISIS])
    print(f"b. Mediana (Valor Central de {COLUMNA_ANALISIS}): {mediana:,.0f}")
    
    # c. Desviación estándar (np.std())
    desviacion_estandar = np.std(df[COLUMNA_ANALISIS])
    print(f"c. Desviación Estándar (Dispersión): {desviacion_estandar:,.0f}")
    
else:
    print(f"Error: La columna '{COLUMNA_ANALISIS}' no es de tipo numérico.")
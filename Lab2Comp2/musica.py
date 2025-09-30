from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# Descarga y descomprime el dataset en la carpeta actual
api.dataset_download_files('mubeenshehzadi/top-100-hits-songs-of-2025', path='.', unzip=True)

print("Descarga completada.")

import pandas as pd
import numpy as np

# Cambia el nombre del archivo si es necesario
df = pd.read_csv('top-100-hits-songs-of-2025.csv')

# Mostrar nombres de columnas para referencia
print("Columnas del dataset:")
print(df.columns)

# 1. Resumen estadístico
print("\nResumen estadístico:")
print(df.describe())

# 2. Tipos de datos
print("\nTipos de datos por columna:")
print(df.dtypes)

# 3. Primeros y últimos registros
print("\nPrimeros registros:")
print(df.head())
print("\nÚltimos registros:")
print(df.tail())

# 4. Ordenar por una columna relevante (ajusta el nombre si es necesario)
columna_orden = 'Streams'  # Cambia por una columna numérica relevante de tu dataset
if columna_orden in df.columns:
    print(f"\nOrdenado por {columna_orden}:")
    print(df.sort_values(by=columna_orden, ascending=False).head())
else:
    print(f"\nLa columna '{columna_orden}' no existe en el dataset.")

# 5. Medidas estadísticas sobre una columna numérica (ajusta el nombre si es necesario)
columna_numerica = 'Streams'  # Cambia por una columna numérica relevante
if columna_numerica in df.columns:
    media = np.mean(df[columna_numerica])
    mediana = np.median(df[columna_numerica])
    desviacion = np.std(df[columna_numerica])

    print(f"\nMedia de {columna_numerica}: {media}")
    print(f"Mediana de {columna_numerica}: {mediana}")
    print(f"Desviación estándar de {columna_numerica}: {desviacion}")
else:
    print(f"\nLa columna '{columna_numerica}' no existe en el dataset.")

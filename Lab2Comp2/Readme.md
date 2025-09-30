INTEGRANTES:
--------------------------------------
**GERSON ASAEL CHICA LOVOS**
---------------------------------------
**ALEJANDRO ERNESTO CHICAS MARTINEZ**

**E kag.py es el que contiene el codigo verdadero los demas fueron pruebas 
y como el tiempo nos quedo corto poreso lo dejamos haci.



a. Describe brevemente de qué trata el dataset utilizado
El dataset youtube-top-100-songs-2025.csv contiene información sobre las 100 canciones más populares de YouTube en el año 2025. Incluye métricas clave como el título del video, el número de vistas (view_count), la duración de la canción, el canal que la publicó y la cantidad de seguidores de dicho canal (channel_follower_count).

b. ¿Qué información permite ver el resumen estadístico?
El resumen estadístico (df.describe()) proporciona una visión clara de la distribución de las columnas numéricas:

Vistas (view_count): La canción promedio tiene ≈106 millones de vistas. Sin embargo, la mediana es mucho menor (≈38 millones), y la desviación estándar es extremadamente alta (≈249 millones). Esto indica una distribución muy asimétrica o sesgada, donde unas pocas canciones tienen un número de vistas excepcionalmente alto (hasta 2 mil millones, el max) que eleva la media.

Duración: El promedio de duración es de ≈204 segundos (alrededor de 3 minutos y 24 segundos).

Seguidores del Canal: Los canales de las 100 canciones principales tienen un promedio de ≈16 millones de seguidores, con un máximo de ≈76.2 millones.

c. ¿Qué cambios o tendencias se detectan en la información del dataset?
Al ver los primeros 5 (head()) y los últimos 5 (tail()) registros, se detecta que las canciones en las primeras posiciones (head()) son, en general, videos de artistas de renombre global (ROSÉ, Bruno Mars, Lady Gaga, Billie Eilish) que tienden a tener un alto número de seguidores en sus canales (hasta 56.8 millones).

Los últimos registros (tail()) muestran una mezcla de artistas con bases de seguidores más pequeñas (ej., HoodTrophy Bino con 20,300 seguidores), lo que sugiere que la clasificación está ordenada por alguna otra métrica no mostrada (como fecha de lanzamiento) o simplemente presenta una lista de videos en el orden de recolección.

d. ¿Qué categorías sobresalen en la comparación y por qué crees que será?
Al realizar el ordenamiento por vistas (view_count) (el Paso 5 completado), las canciones que sobresaldrán serán aquellas con el mayor número de vistas (los videos que se acercan a los 2 mil millones de vistas) y los canales con más seguidores (hasta 76.2 millones).

Razón: Las canciones con el mayor view_count sobresalen porque representan la máxima popularidad y éxito viral. Los canales con más seguidores sobresalen porque tienen una base de audiencia masiva que les garantiza un alto número de vistas rápidamente después de un lanzamiento.

e. ¿Qué diferencias se observan entre los primeros y últimos registros?
(Una vez que el Paso 5 funcione y se ordene por view_count):

Al ordenar por Vistas (Mayor a Menor): Los primeros registros mostrarán canciones con cientos de millones o miles de millones de vistas, mientras que los últimos registros (los menos populares) mostrarán canciones que apenas superan las miles o decenas de miles de vistas (el mínimo es 1,161).

f. ¿Qué aportan las medidas estadísticas al análisis del dataset?
Las medidas estadísticas aplicadas a la columna 'view_count' son esenciales para comprender la popularidad de la música:

Media (≈106M): Muestra el promedio de vistas.

Mediana (≈38M): Muestra que la mitad de las canciones tienen menos de 38 millones de vistas.

Desviación Estándar (≈249M): Su valor, mucho mayor que la media, indica una enorme dispersión y confirma que la lista de las 100 principales no es uniforme. Confirma la existencia de "Outliers" (valores atípicos), que son las pocas canciones virales que han acumulado vistas masivas que distorsionan el promedio.
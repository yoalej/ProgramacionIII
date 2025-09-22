# 🏋️ Calculadora de IMC Flexible - PyQt5

Una aplicación de escritorio en **Python con PyQt5** para calcular el **Índice de Masa Corporal (IMC)** de manera flexible.  

Permite ingresar el **peso y la altura en diferentes unidades** y calcula automáticamente la categoría correspondiente.  

---

## 🎯 Problema a resolver
Muchas personas quieren calcular su IMC, pero no siempre conocen su peso o altura en las mismas unidades:

- Peso: **kilogramos (kg)** o **libras (lb)**  
- Altura: **metros (m)** o **centímetros (cm)**  

Esta aplicación resuelve el problema permitiendo ingresar distintas unidades y obteniendo el **IMC y la categoría** de manera inmediata.

---

## 🛠️ Funcionalidades
- 📌 Calcula IMC ingresando **peso y altura en distintas unidades**.  
- 📌 Determina la categoría automáticamente: **Bajo peso / Normal / Sobrepeso / Obesidad**.  
- 📌 Botón para **calcular IMC**.  
- 📌 Botón para **limpiar campos**.  
- 📌 Manejo de errores con mensajes emergentes en caso de entrada inválida.  
- 📌 Interfaz moderna y amigable, estilo “Redmi”.

---

## 🧩 Widgets usados (PyQt5)
- `QLabel` → etiquetas de nombre, peso, altura y resultado  
- `QLineEdit` → campos de texto para entrada de datos  
- `QPushButton` → botones para calcular y limpiar  
- `QComboBox` → selección de unidades (kg/lb y m/cm)  
- `QMessageBox` → avisos de error  


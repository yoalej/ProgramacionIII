import tkinter as tk
from tkinter import messagebox, ttk

def calcular_imc():
    try:
        nombre = entry_nombre.get()
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        # Convertir unidades si es necesario
        if combo_peso.get() == "lb":
            peso = peso * 0.453592  # lb → kg

        if combo_altura.get() == "cm":
            altura = altura / 100  # cm → m

        if altura <= 0:
            raise ValueError("La altura debe ser mayor que cero")

        # Calcular IMC
        imc = peso / (altura ** 2)
        # Determinar categoría
        if imc < 18.5:
            categoria = "Bajo peso"
        elif imc < 25:
            categoria = "Normal"
        elif imc < 30:
            categoria = "Sobrepeso"
        else:
            categoria = "Obesidad"

        lbl_resultado.config(text=f"{nombre}, tu IMC es {imc:.2f} ({categoria})")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos para peso y altura.")

def limpiar():
    entry_nombre.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    lbl_resultado.config(text="")
    combo_peso.set("kg")
    combo_altura.set("m")

# -------------------------
# Ventana principal
# -------------------------
ventana = tk.Tk()
ventana.title("Calculadora de IMC Flexible")
ventana.geometry("400x350")

# Nombre
tk.Label(ventana, text="Nombre:", font=("Arial", 12)).pack(pady=5)
entry_nombre = tk.Entry(ventana, font=("Arial", 12))
entry_nombre.pack(pady=5)

# Peso
tk.Label(ventana, text="Peso:", font=("Arial", 12)).pack(pady=5)
frame_peso = tk.Frame(ventana)
frame_peso.pack(pady=5)
entry_peso = tk.Entry(frame_peso, font=("Arial", 12))
entry_peso.pack(side=tk.LEFT, padx=5)
combo_peso = ttk.Combobox(frame_peso, values=["kg", "lb"], state="readonly", width=5)
combo_peso.pack(side=tk.LEFT, padx=5)
combo_peso.set("kg")

# Altura
tk.Label(ventana, text="Altura:", font=("Arial", 12)).pack(pady=5)
frame_altura = tk.Frame(ventana)
frame_altura.pack(pady=5)
entry_altura = tk.Entry(frame_altura, font=("Arial", 12))
entry_altura.pack(side=tk.LEFT, padx=5)
combo_altura = ttk.Combobox(frame_altura, values=["m", "cm"], state="readonly", width=5)
combo_altura.pack(side=tk.LEFT, padx=5)
combo_altura.set("m")

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)
btn_calcular = tk.Button(frame_botones, text="Calcular IMC", font=("Arial", 12), command=calcular_imc)
btn_calcular.pack(side=tk.LEFT, padx=10)
btn_limpiar = tk.Button(frame_botones, text="Limpiar", font=("Arial", 12), command=limpiar)
btn_limpiar.pack(side=tk.LEFT, padx=10)

# Resultado
lbl_resultado = tk.Label(ventana, text="", font=("Arial", 12, "italic"))
lbl_resultado.pack(pady=20)

ventana.mainloop()

class Viaje:
    def __init__(self, ruta, costo, tiempo):
        self.ruta = ruta
        self.costo = costo
        self.tiempo = tiempo  # en minutos

    def __str__(self):
        return f"Ruta: {self.ruta} | Costo: ${self.costo:.2f} | Tiempo: {self.tiempo} min"

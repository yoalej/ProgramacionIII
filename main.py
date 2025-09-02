from gestor_viaje import GestorViajes

def main():
    gestor = GestorViajes()

    print("=== Registro de Viajes ===")
    while True:
        ruta = input("Ingrese la ruta de viaje que realizo: ")
        costo = float(input("Ingrese el costo del viaje($): "))
        tiempo = int(input("Ingrese el tiempo (minutos) que tardo en el viaje: "))

        gestor.agregar_viaje(ruta, costo, tiempo)

        continuar = input("¿Desea registrar otro viaje? (si/no): ").lower()
        if continuar != "si":
            break

    gestor.mostrar_viajes()
    gestor.resumen()

if __name__ == "__main__":
    main()

    

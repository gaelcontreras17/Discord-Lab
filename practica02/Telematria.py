# TELEMETRÍA DE CLUSTER IA

def leer_datos():

    temperatura = float(input("Temperatura actual (°C): "))

    memoria = int(input("Uso de Memoria VRAM (%): "))

    enfriamiento = input("¿Enfriamiento activo? (si/no): ")

    return temperatura, memoria, enfriamiento


def diagnostico(temperatura, memoria, enfriamiento):

    if memoria < 0 or memoria > 100:
        print("\nError: Lectura de memoria fuera de rango (0-100%).")

    elif temperatura > 90 or memoria == 100:
        print("\n> Diagnóstico: ¡ALERTA CRÍTICA! Apagando servidores para evitar daños físicos.")

    elif temperatura >= 75 and temperatura <= 90:

        if enfriamiento == "no":
            print("\n> Diagnóstico: Peligro: Temperatura alta y enfriamiento desactivado. Pausando entrenamiento.")

        elif enfriamiento == "si":
            print("\n> Diagnóstico: Temperatura elevada. Reduciendo velocidad de procesamiento (Throttling).")

    elif temperatura < 75 and memoria < 80:

        print("\n> Diagnóstico: Sistema Estable: Entrenamiento en curso a máxima capacidad.")

        memoria_libre = 100 - memoria

        print("> Memoria VRAM disponible:", memoria_libre, "%")


def main():

    print("--- TELEMETRÍA DE CLUSTER IA ---")

    temperatura, memoria, enfriamiento = leer_datos()

    diagnostico(temperatura, memoria, enfriamiento)


if __name__ == "__main__":
    main()
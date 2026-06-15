class MonitorEntrenamiento:
    def __init__(self):
        self.historial_errores = []
        self.umbral_convergencia = 0.01

    def registrar_epoca(self, valor_error):
        if valor_error < self.umbral_convergencia:
            print("[SISTEMA] Entrenamiento completado")
        self.historial_errores.append(valor_error)


def main():
    print("--- Iniciando Monitor ---")

    monitor = MonitorEntrenamiento()
    i = 0

    while i < 5:
        try:
            error = float(input("Ingrese error: "))

            if error < 0:
                print("[ERROR] No negativos")
                continue

            monitor.registrar_epoca(error)
            i += 1

        except ValueError:
            print("[ERROR] Ingresa número")

    print("\n--- Resumen ---")
    print("Historial:", monitor.historial_errores)

    if len(monitor.historial_errores) > 0:
        promedio = sum(monitor.historial_errores) / len(monitor.historial_errores)
        mejor = min(monitor.historial_errores)

        print("Promedio:", promedio)
        print("Mejor:", mejor)


if __name__ == "__main__":
    main()
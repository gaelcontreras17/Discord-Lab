# ESCÁNER BIOMÉTRICO DE IA

def leer_sensor():

    lectura_sensor = []

    for i in range(5):

        dato = int(input("Ingrese bit " + str(i + 1) + ": "))

        lectura_sensor.append(dato)

    return lectura_sensor



def comparar_patrones(patron_maestro, lectura_sensor):

    coincidencias = 0

    for i in range(len(patron_maestro)):

        if patron_maestro[i] == lectura_sensor[i]:
            coincidencias = coincidencias + 1

    return coincidencias



def calcular_porcentaje(coincidencias):

    porcentaje = (coincidencias / 5) * 100

    return porcentaje



def mostrar_estado(porcentaje):

    if porcentaje == 100:
        print("\nESTADO: ACCESO TOTAL: Identidad Verificada.")

    elif porcentaje >= 60:
        print("\nESTADO: ADVERTENCIA: Similitud parcial. Se requiere verificación manual.")

    else:
        print("\nESTADO: ALERTA: Intruso detectado. Sistema bloqueado.")


 
def main():

   
    patron_maestro = [1, 0, 1, 1, 0]

    print("--- ESCÁNER BIOMÉTRICO DE IA ---")

   
    lectura_sensor = leer_sensor()

    print("\n> Comparando lectura con base de datos...")

    
    coincidencias = comparar_patrones(patron_maestro, lectura_sensor)

    
    porcentaje = calcular_porcentaje(coincidencias)

    
    print("\n> Coincidencias encontradas:", coincidencias)

    print("> Porcentaje de Similitud:", porcentaje, "%")

    
    mostrar_estado(porcentaje)

    
    print("\nPatrón Maestro:", patron_maestro)

    print("Lectura Sensor:", lectura_sensor)


if __name__ == "__main__":
    main()
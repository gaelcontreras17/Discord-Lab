
# ANALIZADOR DE SENTIMIENTOS IA


def leer_datos(puntajes_sentimiento):

    for i in range(5):

        print("\nPalabra", i + 1)

        clasificacion = int(input("Clasificación (0: Positivo, 1: Neutral, 2: Negativo): "))

        # Aumentar el valor en la posición correspondiente
        if clasificacion == 0:
            puntajes_sentimiento[0] = puntajes_sentimiento[0] + 1

        elif clasificacion == 1:
            puntajes_sentimiento[1] = puntajes_sentimiento[1] + 1

        elif clasificacion == 2:
            puntajes_sentimiento[2] = puntajes_sentimiento[2] + 1

        else:
            print("Valor inválido")



def buscar_mayor(vector):

    mayor = vector[0]
    posicion = 0

    for i in range(1, len(vector)):

        if vector[i] > mayor:
            mayor = vector[i]
            posicion = i

    return posicion



def mostrar_resultado(posicion):

    if posicion == 0:
        print("\nResultado de IA: La frase es Positiva")
        print("(Predominancia en índice 0)")

    elif posicion == 1:
        print("\nResultado de IA: La frase es Neutral")
        print("(Predominancia en índice 1)")

    elif posicion == 2:
        print("\nResultado de IA: La frase es Negativa")
        print("(Predominancia en índice 2)")



def main():

    
    puntajes_sentimiento = [0, 0, 0]

    print("--- ANALIZADOR DE SENTIMIENTOS IA ---")

    
    leer_datos(puntajes_sentimiento)

    
    print("\nEstado final del vector de características:")
    print(puntajes_sentimiento)

    
    posicion_mayor = buscar_mayor(puntajes_sentimiento)

    
    mostrar_resultado(posicion_mayor)


if __name__ == "__main__":
    main()
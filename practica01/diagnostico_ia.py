# diagnostico_ia.py

import math
from datetime import date


# Procedimiento
def imprimir_encabezado():
    print("====================================")
    print("   SISTEMA DE SALUD INTELIGENTE   ")
    print("====================================")
    print("Fecha:", date.today())
    print()


# Función IMC
def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)


# Función presión
def evaluar_presion(presion_sistolica):
    if presion_sistolica > 140:
        return "Alta"
    else:
        return "Normal"


# Main
def main():
    imprimir_encabezado()

    nombre = input("Nombre del Paciente: ")
    peso = float(input("Peso (kg): "))
    estatura = float(input("Estatura (m): "))
    presion = int(input("Presión Sistólica: "))

    imc = calcular_imc(peso, estatura)
    estado = evaluar_presion(presion)

    print()
    print("--- RESULTADOS DEL ANÁLISIS ---")
    print("Paciente:", nombre)
    print("IMC Calculado:", math.ceil(imc))
    print("Estado de Presión:", estado)
    print("-------------------------------")


if __name__ == "__main__":
    main()
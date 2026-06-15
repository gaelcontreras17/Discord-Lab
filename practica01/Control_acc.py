# control_acceso.py

class ControlAcceso:

    def __init__(self):
        self.usuarios_autorizados = {
            "2024001": "Investigador",
            "2024002": "Estudiante",
            "2024003": "Administrador"
        }

    def verificar_permisos(self, matricula):
        if matricula in self.usuarios_autorizados:
            rol = self.usuarios_autorizados[matricula]
            print("[ACCESO CONCEDIDO] Bienvenido, rol detectado:", rol)

            # Si es administrador puede agregar usuario
            if rol == "Administrador":
                opcion = input("¿Desea agregar nuevo usuario? (si/no): ")

                if opcion == "si":
                    nueva_matricula = input("Nueva matrícula: ")
                    nuevo_rol = input("Rol: ")
                    self.usuarios_autorizados[nueva_matricula] = nuevo_rol
                    print("Usuario agregado correctamente.")

        else:
            print("[ACCESO DENEGADO] Usuario no registrado en la base de datos de IA.")


def main():
    sistema = ControlAcceso()

    print("--- Sistema de Seguridad Laboratorio IA - UX ---")

    try:
        matricula = input("Ingrese su matrícula: ")

        if matricula == "":
            raise ValueError("Campo vacío")

        sistema.verificar_permisos(matricula)

    except ValueError:
        print("Error: Debe ingresar una matrícula.")

    finally:
        print("--- Intento de acceso registrado en el log del servidor ---")


if __name__ == "__main__":
    main()
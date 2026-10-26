# Importación de librerías
import random

# Constantes del juego
PIEDRA = "piedra"
PAPEL = "papel"
TIJERAS = "tijeras"



def decidir_ganador(user_action, computer_action):
    """Determina el resultado de una ronda."""

    # Si ambas jugadas son iguales, hay empate
    if user_action == computer_action:
        return "empate"

    # Si el usuario elige piedra
    if user_action == PIEDRA:
        if computer_action == TIJERAS:
            return "usuario"
        else:
            return "ordenador"

    # Si el usuario elige papel
    elif user_action == PAPEL:
        if computer_action == PIEDRA:
            return "usuario"
        else:
            return "ordenador"

    # Si el usuario elige tijeras
    else:
        if computer_action == PAPEL:
            return "usuario"
        else:
            return "ordenador"


def main():
    """Controla el desarrollo del juego."""

    # Mostrar el título del juego
    print("=== Piedra, papel o tijeras ===")

    # Inicialización de las variables
    jugar = True
    victorias_usuario = 0
    victorias_ordenador = 0
    empates = 0

    # Bucle principal del juego
    while jugar:

        # Pedir la jugada al usuario
        user_action = input(
            "Elige piedra, papel o tijeras (o escribe 'fin' para salir): "
        ).lower().strip()

        # Comprobar si el usuario quiere terminar
        if user_action == "fin":
            jugar = False

        # Comprobar si la jugada es válida
        elif user_action not in (PIEDRA, PAPEL, TIJERAS):
            print("Jugada no válida. Inténtalo de nuevo.")

        # Procesar una jugada válida
        else:
            # PENDIENTE: lógica de la ronda
            pass

    # Mostrar los resultados finales
    # PENDIENTE: mostrar el marcador


# Inicio del programa
if __name__ == "__main__":
    main()


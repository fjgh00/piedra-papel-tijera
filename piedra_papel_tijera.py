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

    # Inicialización de las variables
    jugar = True
    victorias_usuario = 0
    victorias_ordenador = 0
    empates = 0

    # Bucle principal del juego
    while jugar:
        pass


# Inicio del programa
if __name__ == "__main__":
    main()


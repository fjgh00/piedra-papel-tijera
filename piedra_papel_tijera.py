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
    print("\n=== Piedra, papel o tijeras ===")

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
            # Elegir la jugada del ordenador
            computer_action = random.choice((PIEDRA, PAPEL, TIJERAS))

            # Mostrar las jugadas
            print(f"Tú has elegido.........: {user_action}")
            print(f"El ordenador ha elegido: {computer_action}")

            # Determinar el resultado de la ronda
            resultado = decidir_ganador(user_action, computer_action)

            # Mostrar el resultado e incrementar el contador
            if resultado == "usuario":
                print("¡Has ganado esta ronda!\n")
                victorias_usuario += 1
            elif resultado == "ordenador":
                print("El ordenador gana esta ronda.\n")
                victorias_ordenador += 1
            else:
                print("¡Empate!\n")
                empates += 1

    # Mostrar los resultados finales

    # Mostrar los resultados finales
    print("\n=== Marcador final ===")
    print(f"Victorias del usuario: {victorias_usuario}")
    print(f"Victorias del ordenador: {victorias_ordenador}")
    print(f"Empates: {empates}\n")


# Inicio del programa
if __name__ == "__main__":
    main()


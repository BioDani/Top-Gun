import random
from enum import Enum


class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


class GuestYourNumber:
    def __init__(self, difficulty: Difficulty) -> None:
        self.difficulty = difficulty

        if self.difficulty == Difficulty.EASY:
            self.number = random.randint(1, 10)

        if self.difficulty == Difficulty.MEDIUM:
            self.number = random.randint(1, 20)

        if self.difficulty == Difficulty.HARD:
            self.number = random.randint(1, 30)
    
    def run(self):
        number = random.randint(1, 10)
        trials = 0

        # flag variable
        win = False

        while not win:
            guess = int(input("Please enter your guess: "))
            trials += 1

            if guess == number:
                win = True
            elif guess < number:
                print("Too low")
            else:
                print("Too high")
        
        # file = open("scores.txt", "w")
        # file.write(f"Score: {trials}")
        # file.close()
        with open("scores.txt", "w") as file:
            file.write(f"Score: {trials}")

        print(f"You win with {trials} trials")


def main():
    difficulty_map = {
        "easy": Difficulty.EASY,
        "medium": Difficulty.MEDIUM,
        "hard": Difficulty.HARD
    }

    print("Chose the difficulty: ")
    print("1. easy")
    print("2. medium")
    print("3. hard")
    user_input = input("> ")

    difficulty = difficulty_map.get(user_input, Difficulty.MEDIUM)
    game = GuestYourNumber(difficulty)
    game.run()


if __name__ == '__main__':
    main()


# TODO:
# 1. Agregar mas informacion del usuario: Nombre
# 2. Al guardar los puntajes, se guarde con el nombre de usuario y la dificultad
# 3. Al iniciar el juego mostrar un menu con 3 optiones
    # Jugar -> Al usuario elejir este menu, se debe preguntar por una dificultad
    # Mostrar puntajes
    # Creditos
    # Salir

import random

def Play():
    RandomValues = ["Batu", "Kertas", "Gunting"];
    RandomChoice = random.choices(RandomValues, None)
    guess = ""

    print(RandomChoice)

    while guess != RandomChoice[0]:
        guess = str(input("Batu, Kertas atau Gunting? "));
        if guess != RandomChoice[0]:
            print("You lose!");
        elif guess == RandomChoice[0]:
            print("You win!");

Play()
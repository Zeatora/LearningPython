import random

def guess(x):
    random_number = random.randint(1, x);
    guess = 0;
    
    while guess != random_number:
        guess = int(input("Please input your guess: "));
        print(random_number);
        if guess > random_number:
            print("Too high!");
        elif guess < random_number :
            print("Too low!");
    print("Congratulations u did it!")
    

guess(100)
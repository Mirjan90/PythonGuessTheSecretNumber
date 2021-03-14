#GUESS THE SECRET NUMBER

import random

secret = int(random.randint(0 , 19));

number = int(input("Guess the secret number (between 1 and 20): "))

if secret == number:
        print("You have guessed it")

else:
    print("Not a correct number. Correct number is: " + str(secret))

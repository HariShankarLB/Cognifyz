# Task1: Write a Python program that generates a random number between 1 and 100. The user should then try to guess the number. The program should provide hints such as "too high" or "too low" until the correct number is guessed.

# Task2: Create a number guessing game where the program generates a random number between a specified range, and the user tries to guess it. Provide feedback to the user if their guess is too high or too low.

import random as r

start=1
end=100
target=r.randint(start,end)
count=0

print(f"Guessing Number game\nThe number is inbetween {start} and {end}")

while True:

    user=int(input("Enter Number: "))
    count += 1

    if user>end or user<start:
        print(f"please enter number inbetween {start} and {end}")

    elif user>target:
        print("Too high")

    elif user<target:
        print("Too low")
    
    else:
        print("Congratulations! You have guessed the number")
        print(f"You took {count} attempt")
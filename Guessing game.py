import random

secret=random.randint(1,100)
attempts=0


while attempts<7:
    guess = int(input("Enter the number:"))
    attempts +=1


    if guess > secret:
        print("The number is too high")

    elif guess< secret:
        print("The number is too low")

    elif guess== secret:
        print(f"Bravo! Found in {attempts} attempts")
        break 


if guess != secret:
    print("Lost! It was", secret)       

import random
number = random.randint(1,50)
guess = int(input("Enter a number between 1 to 50: "))
while guess != number:
    if guess <= number:
        print("You need to guess highest number.Try again")
        guess = int(input("Enter a number between 1 to 50: "))
    else:
        print("You need to guess lowest number.Try again")
        guess = int(input("Enter a number between 1 to 50: "))
print("You guessed correctly!")



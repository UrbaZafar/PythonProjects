import random

def numbers():
    attempts=0
    guess=None
    num=random.randint(1,100)

    while guess!= num:
        guess=int(input("enter the number or guess"))
        attempts +=1

        if guess < num:
            print("low")
        elif guess> num:
            print("high")
        else:
            print("waoo")

numbers()

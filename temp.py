def fahrenheit():
# used tp convert celsius to fahrenheit
    Celsius=float(input("Enter your number\n"))
    far=(Celsius*9/5)+32
    print(f"this is used to covert celsius {Celsius} to fahrenheit{far}")


def celsius():
# used to convert fahrenheit into celsius
    Fare=float(input("Enter your number\n"))
    Cel=(Fare-32)*9/5
    print(f"this is used to covert {Fare} fahrenheit into {Cel} celsius")


def choice():
    user=input("Tell u want function fc or cf\n").strip().lower()

    if user.strip() == "cf":
       fahrenheit()
    elif user.strip() == "fc":
        celsius()
    else:
        print("INVALID CHOICE")

    choose=input("do you want to go again?\n").strip().lower()
    if choose=="yes":
        choice()
    else:
        print("terminate")

choice()

    
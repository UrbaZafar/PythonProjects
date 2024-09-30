def menu():
    print("Steak")
    print("burger")
    print("rice")

    choice= input("Enter your choice from the menu").strip().lower()
    if choice=="Steak":
        print("it will take 20 minutes")
    elif choice=="burger":
        print("it will take 10 minutes")
    elif choice == "rice":
        print("it will take 5 minutes")
    else:
        print("OKay no order,do you want some drinks")

    drinks=input("enter your drink choice").strip().lower()
    print(f"this your {drinks}")

    opinion=input("please give our resturant a rating 1star,2star....5star").strip().lower()
    if opinion=="1star":
        print("we will try to make it better")
    elif opinion == "2star":
        print("we will do our best")
    elif opinion =="3star":
        print("thank you")
    elif opinion == "4star":
        print("we are delighted to have your opinion")
    elif opinion == "5star":
        print("heart")
    else:
        print("remeber the name")
    
    print("thank you for your visit, dubara aya")


menu()
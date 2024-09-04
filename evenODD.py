def number():
    num= int(input("enter your number"))
    if num %2==0:
        print("even")
    else:
        print("odd")

# strip is used to remove the white spaces and lower is used to remove 
# the upper and lower case thing

# why it was not running before?
# beacuzse when i type yes it includes spaces and system interpet and cosider it fasle
# so strip changes tha and now my code and run succesfully

    choice =str(input("do you want to go again yes /NO")).strip().lower()
    if choice == "yes":
        number()
    else:
        print("terminate")
 
number()

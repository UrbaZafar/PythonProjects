import sys
print("Welcome to crore patti kbc")
print("are you thrilled to play this game")

choice=input("do you want to play this game?")
if choice=="yes":
    print("let,s go")
else:
    print("terminate")
    sys.exit()
print()
price=0
question1=["What is the chemical symbol for the element gold?"]
print("the reward of this question is 500rp")
print(question1)
answer1=(input("Enter your answer:"))
if answer1.lower() == "au":
    print("correct,you have won 500 ruppes")
    price+=500
else:
    print(" no,the answer is au")
print()

question2=["What bird is a symbol of wisdom in many cultures?"]
print("the reward of this question is 2000rp")
print(question2)
answer2=(input("Enter your answer:"))
if answer2.lower() == "owl":
    print("correct,you have won 2000 ruppes")
    price+=2000
else:
    print(" no,the answer is owl")
print()


question3 = "What instrument does a musician typically play by blowing air through its pipes?"
print("The reward for this question is 5000rp")

print(question3)
answer3 = input("Enter your answer: ")
if answer3.lower() == "flute":
    print("Correct! You've won 5000rp.")
    price += 5000
else:
    print("Incorrect. The correct answer is 'flute'.")
print()

question4=["What mammal is the only flying mammal?"]
print("this question is 10000 ruppes worth")
print(question4)
answer4= input("Enter your answer:")
if answer4.lower()== "bat":
    print("your answer is correct,you won 10000 ruppes")
    price+=10000
else:
    print("wrong,the correct is bat and loose 10000")

print("the total reward is",price,"ruppes")
print()
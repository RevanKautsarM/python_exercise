import random

print( "Welcome to the Coin Flipping Game!")

choice=input("Enter your side (Head or Tail): ")

num=random.randint (1, 2)

if num==1:
    result="Head"

elif num==2:
        result="Tail"

if choice==result:
    print("Good Job! You Won. The coin flipped", result)

else:
    print("Aw... You lost. The coin flipped", result)

print("Thanks for Playing. Goodbye")
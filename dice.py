#hello random
import random
while 1:
 print("Hello, Lets play dice game")
 play = input("Do you want to play, if yes Press Y").lower()
 def dice() :
    roll = random.randint(1,6)
    return roll
 if play == "y":
    result = dice()
    print("you got",result)
 else:
    print("Fuck off")
    exit()




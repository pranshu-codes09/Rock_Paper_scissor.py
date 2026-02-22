import random
computer = random.choice([1, 2 ,3])
print('''1 = rock
2 = paper
3 = scissor''')

you = int(input("enter your choice:"))
youdict = {1:"rock ",2:"paper",3:"scissor"}
print (f"you choosed {youdict[you]}")
print (f"computer choosed {youdict[computer]}")

if (computer == you):
    print("It's a tie 🙌")
else:
    if (computer == 1 and you == 2):
        print("you won!🥳")
    elif (computer == 1 and you == 3):
        print("you lose!😐")
    elif (computer == 2 and you == 1):
        print("you lose!😐")
    elif (computer == 2 and you == 3):
        print("you won!🎊🥳")
    elif (computer == 3 and you == 1):
        print("you won!🎊🎉")
    elif (computer == 3 and you == 2):
        print("you lose!😔")
    

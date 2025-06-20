#Machine generate a number between 1 to 100
#Loop
#user guess the number by giving input
#if user input is not numeric or between 1 to 100 print invlaid
#if user input is between 1 to 100 then give the feedback Too High or Too low
#once user input matches with the generated number give congratualtion message in which try
import random
machNum =random.randint(1,100)
tries=0
while True:
    userNum = input("Guess the number between 1 and 100:")
    tries+=1
    if not(userNum.isnumeric()):
        print("Please enter a valid number")
        tries-=1
    else:
        userNum=int(userNum)
        if userNum not in range(1,101):
            print("Please enter a valid number")
            tries-=1
        elif machNum<userNum:
            print("Too High!")
        elif machNum>userNum:
            print("Too Low!")
        elif machNum==userNum:
            print(f"Congratulations! You guessed the number in {tries}th try ")
            break

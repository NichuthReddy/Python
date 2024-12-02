#Loop
    #generate R/P/S
    #input R/P/S
    #if not R/P/S then print invalid choice
    #else 
        #Print your choice is R
        #Comupter choice is S
        #Computer or You Win using WinLoss fucntion
        #if(input Do you want to play again(y/n)='n')
        #break

#Create function for WinLoss
# if Comp_Choic= Your_choice then print draw
# elif (Your_choice,Comp_choice) in [(R,S),(P,R),(S,P)] then Print You Win
# else Print computer win
import random

def WinLoss(your_choice,computer_choice):
    if your_choice==computer_choice:
        print("you draw with the Computer")
    elif (your_choice,computer_choice) in [('R','S'),('P','R'),('S','P')]:
        print("You Win")
    else:
        print("Computer Win")
        
if __name__=="__main__":
    while True:
        computer_choice=random.choice(['R','P','S'])
        while True:
            your_choice=input("rock, paper or scissors? (r/p/s):").upper()
            if your_choice not in ['R','P','S']:
                print("invalid choice")
            else:
                break
        WinLoss(your_choice,computer_choice)
        if input("Do you want to play again? (y/n):")=='n':
            break

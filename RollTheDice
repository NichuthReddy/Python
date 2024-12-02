from random import randrange,choice 
def RollTheDice(choice):
    if choice.lower()=="y":
        print(randrange(1,7),randrange(1,7))
    elif choice.lower()=="n":
        print("Thanks for playing!")
        return
    else:
        print("Invalid Choice!")
    choice=input("Roll the Dice? (y/n):")
    return RollTheDice(choice)
    
if __name__=="__main__":
    choice=input("Roll the Dice? (y/n):")
    RollTheDice(choice)

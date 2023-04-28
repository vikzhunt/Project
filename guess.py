import random as r
print("------------------- Greetings !! -----------------")
def guess():
    lvl=input("Difficulty Level : \n1. Advance\n2. Moderate\n3. Beginner\nEnter difficulty level : ")
    print("-----------------------------------------------------------------")
    if lvl=="1":
        print("Guess The Number between 1 to 100")
        print("No. of Attempts : 5")
        c=r.randint(1,100)
        for i in range(5):
            a=int(input("Enter your no. : "))
            if a==c:
                print("-----------------Hurray!,you have guessed the number.")
                print("SCORE : ",2*(5-i),"/",10)
                break
            elif a>c:
                print("Too High\nTry Again")
                print("No. of attempts left ",4-i)
                print("-----------------------------------------------------------------")
            elif a<c:
                print("Too Low\nTry Again")
                print("No. of attempts left ",4-i)
                print("-----------------------------------------------------------------")
        else:
            print("SCORE : 0/10 \nOH! You have lost. BETTER LUCK NEXT TIME")
            print("Correct answer was ",c)
            print("-----------------------------------------------------------------")
    elif lvl=="2":
        print("Guess The Number between 1 to 100")
        print("No. of attempts : 10")
        c=r.randint(1,100)
        for i in range(10):
            a=int(input("Enter your no. : "))
            if a==c:
                print("-----------------Hurray!,you have guessed the number.")
                print("SCORE : ",10-i,"/",10)
                break
            elif a>c:
                print("Too High\nTry Again")
                print("No. of attempts left ",9-i)
                print("-----------------------------------------------------------------")
            elif a<c:
                print("Too Low\nTry Again")
                print("No. of attempts left ",9-i)
                print("-----------------------------------------------------------------")
        else:
            print("SCORE : 0/10 \nOH! You have lost. BETTER LUCK NEXT TIME")
            print("Correct answer was ",c)
            print("-----------------------------------------------------------------")
    elif lvl=="3":
        print("Guess The Number between 1 to 100")
        c=r.randint(1,100)
        ct=0
        while 1:
            a=int(input("Enter your no. : "))
            if a==c:
                print("-----------------Hurray!,you have guessed the number.")
                print("SCORE : ",100-ct,"/",100)
                break
            elif a>c:
                print("Too High\nTry Again")
                print("-----------------------------------------------------------------")
                ct=ct+1
            elif a<c:
                print("Too Low\nTry Again")
                print("-----------------------------------------------------------------")
                ct=ct+1
    else :
        print("Enter a valid choice.")
    m=input("Do you want to play again ( Yes or No ): ").capitalize()
    if m=="Yes":
        guess()

ch=input("READY TO PLAY THE GAME\nEnter Yes or No : ").capitalize()
if ch=="Yes":
    guess()
    
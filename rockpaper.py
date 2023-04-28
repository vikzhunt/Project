import random as r
print("------------------- Greetings !! -----------------")
def rps():
    print("------------------- ROCK PAPER SCISSORS -------------------")
    print("RULES :\n\n1. Rock vs Scissors : Rock Wins\n2. Rock vs Paper    : Paper Wins\n3. Scisors vs Paper : Scissors wins")
    print()
    print("Enter your choice acc. to the condition mentioned below :-")
    print()
    print("Enter 1 for Rock\nEnter 2 for Paper\nEnter 3 for Scissors.")
    c=r.randint(1,3)
    if c==1:
        v="Rock"
    elif c==2:
        v="Paper"
    elif c==3:
        v="Scissors"
    print("----------------------------------------------------")
    a=int(input("Enter your choice : "))
    if a==1:
        u="Rock"
    elif a==2:
        u="Paper"
    elif a==3:
        u="Scissors"
    else:
        print("Enter a valid choice.")
    if c==a:
        print("----------- DRAW -----------")
    elif c==1 and a==2 :
        print("Your choice : ",u,"\nComputer choice : ",v)
        print("*-------- YOU WIN --------*")
    elif c==1 and a==3:
        print("Your choice : ",u,"\nComputer choice : ",v)
        print("*-------- COMPUTER WIN --------*")
    elif c==2 and a==1:
        print("Your choice : ",u,"\nComputer choice : ",v)
        print("*-------- COMPUTER WIN --------*")
    elif c==2 and a==3:
        print("Your choice : ",u,"\nComputer choice : ",v)
        print("*-------- YOU WIN --------*")
    elif c==3 and a==1:
        print("Your choice : ",u,"\nComputer choice : ",v)
        print("*-------- YOU WIN --------*")
    elif c==3 and a==2:
        print("Your choice : ",u,"\nComputer choice : ",v)
        print("*-------- COMPUTER WIN --------*")
    m=input("Do you want to play again Yes or No : ").capitalize()
    if m=="Yes":
        rps()
ch=input("READY TO PLAY THE GAME\nEnter Yes or No : ").capitalize()
if ch=="Yes":
    rps()
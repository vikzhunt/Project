import random as r
print("------------------- Greetings !! -----------------")

while True:
    n=int(input("Enter length of OTP : "))
    c=r.randint(10**(n-1),10**(n)-1)
    print("-----------------------------------------")
    print('Your OTP is : ',c)
    print("-----------------------------------------")
    print('DO YOU WANT TO GENERATE ANOTHER OTP :- \nYes or No')
    ch=input('Enter your Choice : ').capitalize()
    if ch=='Yes':
        continue
    elif ch =='No':
        break
    else:
        print("Enter a valid choice")

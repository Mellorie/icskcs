#Write a program in python to accept an integer and perform following operations
#a)Main program to accept an integer number to check prime , palindrome and print multiplication table.Repeat based on users choice
#b)function prime() to accept a number as a parameter and print whether number is prime or no
#c)a function palindrome() to accept a number as a parameter and print whether is palindrome or no
#d)a function multi() to accept a number as a parameter and print multiplication table for 10 times.

def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            print(n,"Is not a Prime Number")
            break
        else:
            print(n,"Is a Prime Number")
            break
def palindrome(p):
    r=0
    temp=p
    while p!=0:
        p=p//10
        if r==tem:
            print(tem,"Is a Palindrome Number")
        else:
            print(tem,"Is not a Palindrome Number")
def multi(a):
    print('='*68)
    for i in range(1,11):
        p=f"{i:>25d}{'x'}{a}{'='}{i*a:<2d}"
        print(p)
        print('='^68)
print("***MAIN MENU***")
print("1.Prime ")
print("2.Palindrome")
print("3.Multiplication Table")
print("4.Exit")
while True:
    ch=int(input("enter Your Choice"))
    print()
    if ch==1:
        a=int(input("Enter Number="))
        prime(a)
    elif ch==2:
        a=int(input("Enter Number="))
        palindrome(a)
    elif ch==3:
        a=int(input("Enter Number="))
        multi(a)
    if ch==4:
        a=int(input("Enter Number="))
        print("Thanks For Using")
        break
else:
        print("Invalid Option")
    
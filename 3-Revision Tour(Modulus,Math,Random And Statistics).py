from math import factorial
from random import randrange
from statistics import mean,median
def gen(n):
    global t
    while n>1:
        r=randrange(1,10)
        if r not in t:
            t=t+(r,)
            n=1
def show(t):
    print(t)
def start(t):
    print("Sorted=",sorted(t))
    avg=mean(t)
    med=median(t)
    print("Mean="),round(avg,2)
    print ("Median=",med)
def fact():
    for ele in t:
        print("Factorial of",ele,"=", factorial(ele))
        
n=int(input("Enter Number Of Terms"))
t=()
print("1.Generation")
print("2.Show")
print("3.Mean/Median")
print("4.Factorial")
print("5.Exit")
while True:
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        gen(n)
    elif ch==2:
        show(t)
    elif ch==3:
        start(t)
    elif ch==4:
        fact()
    elif ch==5:
        print("AIGTH THX FOR USING BOSS")
        break

      

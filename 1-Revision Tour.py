#write a program in python to calc area and circ of a circle as per requirements
#a) main program accept 3 radius and print results using bigger radius as an arguement
#b) func big_two() to accept 2 parameters and return bigger of 2 numbers
#c) func big_three() to accept 3 paramters and return the bigger of 3 numbers by invoking func big_two()
#d) a func cal() to accept radius as parameter and return area and circumference
import math
def big_two(x,y):
    if x>y:
        return x
    else:
       return y

def big_three(a,b,c):
    return big_two(a,big_two(b,c))
def cal(r):
    a=round(math.pi*r*r,2)
    c=round(2*math.pi*r,2)
    return a,c
while True:
    r1=int(input("Enter 1st No"))
    r2=int(input("Enter 2nd No"))
    r3=int(input("Enter 3rd No"))
    b=big_three(r1,r2,r3)
    a,c=cal(b)
    g2=""*2
    g3=""*3
    print("="*34)
    h=f"{'Three':10s}{g3}{'circumference':*>6s}" 
    print(h)
    print("-"*34)
    p=f"{r1:>2d}{g2}{r2:2d}{g2}{r3:>2d}{g3}{b:^3d}{g3}{a:>6.2f}{g3}{c:>6.2f}"
    print(p)
    print("-"*34)
    ans=input("want to continue?[y/n]")
    if ans.lower=='n':
        break
        
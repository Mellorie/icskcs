Only3_5=[]
def push3_5(N):
    for no in N:
        if no%3==0 or no%5==0:
            only3_5.append(no)
        print(only3_5)
    
def pop3_5():
    if only3_5==[]:
        print("Underflow")
    while only3_5!=[]:
        print(only3_5.pop())
    else:
        print("Stack empty")
        
N=[]
def make_list():
    global N
    N=[]
    for i in range(5):
        no=int(input("Enter No:"))
        N.append(no)
        
while True:
    print("\n 1.Make list \n 2.Push list \n 3.Pop list \n 4.Exit")
    ch=int(input("Enter Your Choice:"))
    if ch==2:
        push3_5(N)
    elif ch==3:
        pop3_5()
    elif ch==1:
        makelist()
    else:
        break

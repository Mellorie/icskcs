Only3_5=[]
def push3_5(N):
    for no in N:
        if no%3==0 or no%5==0:
            only3_5.append(no)
        print(only3_5)
    
def pop3_5():
    if only 3_5==[]:
        print("Underflow")
    while only 3_5!=[]:
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
    print("\n 1.Makelist \n 2.Pushlist \n 3.Poplist \n 4.Exit")
    ch=int(inpout("Enter Your Choice:"))
    if ch==2:
        push 3_5(N)
    elif ch==3:
        pop 3_5()
    elif ch==1:
        makelist()
    else:
        break

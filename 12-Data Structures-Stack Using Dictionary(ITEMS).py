def push(SItems):
    Item=[]
    count=0
    for name,price in SItems.Items():
        if price>75:
            Item.append(name)
            count+=1
        print(f"Stack Contain:{Item}")
        print(f"The count of elements in stack is {count}")

def pop_stack(Item):
    if Item==[]:
        print("Stack Empty")
    else:
        while Item!=[]:
            print(Item.pop())
    print("Stack Is Now Empty")
    
DIT={}
n=int(input("Enter No of Items:"))
for i in range(n):
    name=input("Enter Name of Items")
    price=input("Enter price of items:")
    DIT[name]=price
stack=[]
while True:
    print("1.Push \n 2.Pop \n 3.Exit")
    ch=int(input("Enter Choice:"))
    if ch==1:
        stack=push(DIT)
    elif ch==2:
        Pop_stack(stack)
    else:
        break
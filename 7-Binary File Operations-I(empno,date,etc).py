import pickle

def create():
    file=open("emp.dat","wb")
    n=int(input("Enter No. Of Employees:"))
    for i in range(n):
        rno=int(input("Enter Empno:"))
        name=int(input("Enter Name:"))
        dept=input("Enter Department")
        sal=float(input("Enter Salary:"))

L=[eno,name,dept,sal]
pickle.dump(L,file)
file.close()

def Display():
    file=open("emp.dat","rb")
    L=[]
    file.seek(0,2)
    epos=file.tell()
    file.seek(0)

while True:
    if file.tell()==epos:
        break
    L=pickle.load(file)
    print("%-3d"%L[0],"%-10s"%L[1],"%-10s",%L[2],"%7.2d"%L[3])
file.close()
    
    def search():
        file=open("emp.dat","rb")
        L=[]
    file.seek(0,2)
    epos=file.tell()
    file.seek(0)
    dep=input("Enter Department:")
    flag=False
    
while True:
    if file.tell()==epos:
         break
    L=pickle.load(file)
     if dep.lower()==L[2].lower():
         print("%-3d"%L[0],"%-10s"%L[1],"%-10s",%L[2],"%7.2d"%L[3])
         flag=True
if flag==False:
    print("record not Found")
    
file.close()

while True:
    print("1.Create")
    print("2.Display")
    print("3.Search")
    print("4.Exit")
    ch=int(input("Enter Your Choice:"))
if ch==1:
    create()
elif ch==2:
    Display()
elif ch==3:
    search()
else:
    break
            
            
        
        
        
        
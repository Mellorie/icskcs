import pickle
def create():
    with open("student.dat","wb") as file:
        details={}
        n=int(input("Enter No. Of students:"))
        for i in range(n):
            rno=int(input("Enter roll no:"))
            en=int(input("Enter English Marks:"))
            phy=int(input("Enter Physics MArks:"))
            mat=int(input("Enter Math Marks"))
            che=int(input("enter Chemistry Marks:"))
            cs=int(input("Enter CS marks"))
            details[rno]=[en,phy,che,mat,cs]
        pickle.dump(d,file)
def display():
    with open("Student.dat","rb") as file:
        try:
            while True:
                d=pickle.load(file)
                for k,v in d.items():
                    print("roll No:",k)
                    print("Eng:",v[0],"\n Physics:",v[1],"\n Chemistry",v[2],"\n Math:",v[3],"\n(s:"v[4])
                    print("Total Marks:",v[0]+v[1]+v[2]+v[3]+v[4])
         except EOFError:
             print("Done")
def Output():
    with open("Student.dat","rb") as file:
        rn=int(input("Enter Roll No. To Seach"))
        flag=FAlse
        try:
            while True:
                d=pickle.load(file)
                for k,v in d.items():
                    if rn==k:
                        print("Eng:",v[0])
                        print("Phy:",v[1])
                        print("Mat:",v[2])
                        print("Che:",v[3])
                        print("cs:",v[4])
                        Total=v[0]+v[1]+v[2]+v[3]+v[4]
                        print("Total:",Total)
                        flag=True
        except EOFError:
             print("Finished")
        if flag==False:
            print("Record Not Found")
while True:
    print("1.Create \n 2.Display \n 3.Search \n 4.Exit")
    op=int(input("Enter Your Choice:"))
    if op==1:
        create()
    elif op==2:
        display()
    elif op==3:
        output()
    else:
        break
    
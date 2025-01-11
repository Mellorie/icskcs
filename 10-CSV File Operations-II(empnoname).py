import csv
def create():
    with open("employee.csv",mode='w',newline="") as file:
        mywrite=csv.writer(file)
        n=int(input("Enter No. Of Records:"))
        for i in range(n):
            empno=int(input("Enter Employee No:"))
            ename=input("Enter Employee Name:")
            salary=int(input("Enter Salary:"))
            mywriter.writerow((empno,ename,salary))

def heading():
    print('-'*45,f"{'Employee No':<15s}{'Employee name':^15s}{'Salary':>15s}n",'-'*45)
def display_tot():
    with open("employee.csv") as file:
        myreader=csv.reader(file)
    totsal=totemp=0
    heading()
    for row in myreader:
        print(f"{row[0]:<15s}{row[1]:^15s}{row[2]:>15s}")
        totsal+=int(row[2])
        totemp+=1
    print("Total Employees:",totemp)
    print("Total Salary:",totsal)

while True:
    print("\n\n 1.Create \n 2.Display All \n 3.Display Total \n 4.Exit")
    ch=int(input("Enter Your Choice:"))
if ch==1:
    create()
elif ch==2:
    display_all()
elif ch==3:
    display_tot()


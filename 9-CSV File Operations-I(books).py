import csv
def create():
    date=()
    print('-'*60)
    num=int(input("Enter  No. Of Books:"))
    for i in range(num):
        code=input("enter Book Code:")
        name=input("Enter book name:")
        price=float(input("Enter book price"))
        data+=((code,name,price))
        print("-"*60)
        with open('books.csv','w',newline='') as file:
            writer=csv.writer(file)
            writer.writerows(data)
    
def display_all():
    with open('books.csv','r') as file:
        reader=csv.reader(file)
        print('-'*60)
        for row in reader:
                  print(f"{row[0]} {row[1]:<30}{row[2]:<15}")
                  print("-"*60)
def display_index():
    with open('books.csv','r') as file:
        reader=csv.reader(file)
    books_found=False
    print(f"{'Book Code'}\t\t{'Name':<30}{'price':<15}")
    for row in reader:
        if float(row[2])>10:
            print(f"{row[0]}\t\t{row[1]:<30}{row[2]:<15}")
            books_found=True
            print('-'*60)
            if books_found==False:
                print("No Book Available")
                print('-'*60)
print('-'*60)
print("1.Book Details \n 2.Display All Books \n 3.Display Book Details with price >10 \n 4.EXIT")
print('-'*60)

while True:
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        create()
    elif choice==2:
        display_all()
    elif choice==3:
        display_index()
    else:
        break
           
                    
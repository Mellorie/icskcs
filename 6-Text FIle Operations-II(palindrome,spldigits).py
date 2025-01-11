def acc():
    file=open("info 35c.txt","w")
    LST=[]
    while True:
        st=input("enter a string:")
        if st==():
            break
        file.writelines(LST)
        file.close()
    
def palin():
    file=open("info.txt","r")
    lnest=file.readlines()
    pl=[]
    for ln in lnest:
        for w in ln.split():
            if w[0:]==w[::-1]:
                pl.append(w)
print("Text File=",lnest)
print("palindrome words",pl)
file.close()

def check():
    file=open("info.txt","r")
    lnest=file.readlines()
    u=s=d=0
    for ln in lnest:
        for ch in ln:
            if  ch in ln:
                if ch.isupper():
                    u+=1
                elif not ch.isalnum() and ch!="":
                    s+=1
                elif ch.isdigit():
                    d+=1
    
print("Text File=",lnest)
print("No of upper=",u)
print("No of Special Characters=",s)
print("No of Digits=",d)
file.close()

while True:
    print("1.Accept")
    print("2.Palindrome")
    print("3.Check")
    print("4.Exit")
    ch=int(input("Enter Your Choice"))
    if ch==1:
        acc()
    elif ch==2:
        palin()
    elif ch==3:
        check()
    else:
        break
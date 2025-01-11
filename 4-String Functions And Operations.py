def acc():
    global st
    st=input("Enter string")
def palin(st):
    if st[0:]==st[::-1]:
        print("IT IS A PALINDROME")
def check(st):
    u=l=s=d=0
    for t in st:
        if t.isupper():
            u+=1
        elif t.islower():
            l+=1
        elif not (t.isalnum()) and t!="":
            s+=1
        elif t.isdigit():
            d+=1
        print("no of lower=",l)
        print("no of upper=",u)
        print("no of spelchar=",s)
        print("no of digits=",d)
def cnt(st):
    v=c=0
    for ch in st:
        if ch.isalpha():
            if ch in "AEIOUaeiou":
                v+=1
            else:
                c+=1
    print("No of voewls:",)
    print("no of consonants:",c)
st=""
while True:
    print("1.acccept")
    print("2.Palindrome")
    print("3.check")
    print("4.Count Vow and COns")
    print("5.exit")
    ch=int(input("ENter Your choice"))
    if ch==1:
        acc()
    elif ch==2:
        palin(st)
    elif ch==3:
        check(st)
    elif ch==4:
        cnt(st)
    else:
        break
    
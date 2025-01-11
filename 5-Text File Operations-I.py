def acc():
    st=input("Enter a String :")
    file=open("info.txt", "w")
    file.write(st)
    file.close()

def checkword():
    word= input("Input a word :")
    c=0
    file = open("info.txt","r")
    st =file.read()
    for w in st.split():
        if w==word:
            c+=1
        print("string:",st)
        print(word,"Exists for",c,"times")
        file.close()
    
    def checkvowel():
        v=0
        file=open("info.txt","r")
        st=file.read()
        for w in st.split():
            if w[0] in "AEIOUaeiou":
                v+=1
            print("string:",st)
            print("No of words starting with v")
            file.close()
            
while True:
    print("1.Accept")
    print("2.Check Word")
    print("3.Check Vowel")
    print("4.Enter")
    ch=int(input("Enter Your Choice"))
    if ch==1:
        acc()
    elif ch==2:
        checkword()
    elif ch==3:
        checkvowel()
    else:
            break

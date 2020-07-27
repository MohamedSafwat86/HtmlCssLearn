def EvenOrOdd():
    try:
        n=int(input("Enter a number: "))
        if n%2 ==0:
            print("Even number")
        else:
            print("Odd number")
    except Exception:
        print("Error")

def StringCopy():
    try:
        n=int(input("Enter a number of copies: "))
        st =input("Enter string: ")
        if(len(st) >2):
            print(n*st[:2])
        else:
            print(n*st)
    except Exception:
        print("error")

def IsVowel():
    try:
        L=input("Enter a letter: ")
        assert len(L)==1
        L=L.lower()
        if L[0]=="a" or L[0]=="e" or L[0]=="i" or L[0]=="u" or L[0]=="o" or L[0]=="y":
            print("Vowel")
        else:
            print("No Vowel")
    except Exception:
        print("error")

def InRange():
    st=input("Enter range: ")
    s=input("value:")
    print(s in st.split(","))
         


#EvenOrOdd()
#StringCopy()
#IsVowel()
InRange()

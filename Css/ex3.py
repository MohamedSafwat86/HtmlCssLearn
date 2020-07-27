def larger_string(str, n):
    try:
        assert n>=0
        return str*n
    except Exception:
        print("error")

try:
    d=int(input("Enter a number"))
    if d>17:
        print(2*abs(d-17))
    else:
        print(abs(d-17))
except ValueError:
    print("Error")

try:
    d=int(input("Enter a number"))
    d1=int(input("Enter a number"))
    d2=int(input("Enter a number"))
    sum=d+d1+d2
    if (d==d1) and (d1==d2) :
        print(3*sum)
    else:
        print(sum)
except ValueError:
    print("Error")

st=input("Enter String: ")
if(st.split(" ")[0]=="Is"):
    print(st)
else:
    print("Is "+st)

print(larger_string("abc",5))

import calendar
from datetime import date,timedelta
from math import pi

def GetDiffDays():
    date1=input("Enter date1 in format DD-MM-YYYY: ")
    date1list = date1.split("-")
    date2=input("Enter date2 in format DD-MM-YYYY: ")
    date2list = date1.split("-")
    date2list = date2.split("-")
    t =timedelta()
    try:
        t=date.fromisoformat("{0}-{1:02n}-{2:02n}".format(date2list[-1],int(date2list[1]),int(date2list[0])) ) - date.fromisoformat("{0}-{1:02n}-{2:02n}".format(date1list[-1],int(date1list[1]),int(date1list[0])) )
        print(t.days)
    except Exception:
        print("Error")
        
def SphereVolume():
    try:
        r=float(input("Sphere raduis:"))
        print((4*pi*r**3)/3)
    except Exception:
        print("error")
    


   

n= input("Enter an interger: ")
try:
    print(int(n)+int(n*2)+int(n*3))
except ValueError:
    print("Input error")

help(abs)
cal = calendar.TextCalendar()
print(cal.formatmonth(2020,7))
print(date.today().strftime("%d %B %Y"))
print('''a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example''')
SphereVolume()
GetDiffDays()


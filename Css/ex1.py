import platform
from datetime import datetime
import math
def CirculeArea():
    try:
        r=float(input("Please enter a radias"))
        print("Area is:{0}".format(math.pi*(r**2)))
    except ValueError:
        print("Input is not number")
    except Exception:
        print("Some thing went wrong")


exam_st_date = (11, 12, 2014)
print("The examination will start from :",datetime(exam_st_date[-1],exam_st_date[1],exam_st_date[0]).strftime("%d/%m/%Y"),sep=" ")
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")
print(platform.python_version())
print("Current date and time :\n{0}".format(datetime.today().strftime("%d/%m/%Y  %H:%M:%S")))
CirculeArea()
first=input("First Name: ")
last=input("Last Name: ")
print(last,first,sep=" ")
sam= input("Sample: ")
print(sam.split(","))
print(tuple(sam.split(",")))
filename=input("Enter File Name:")
print((filename.split("."))[1])
color_list = ["Red","Green","White" ,"Black"]
print("First color: {0}".format(color_list[0]),"Last Color: {0}".format(color_list[-1]),sep=" ")



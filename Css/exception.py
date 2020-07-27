def readint(prompt, min, max):
    try:
        while True:
            number=int(input(prompt))
            assert number<=max and number >= min
            return number
    except (ValueError):
            print("Error: wrong input")
    except AssertionError:
            print("Error: the value is not within permitted range ({0}..{1})",min,max)
            
        
#
# put your code here
#
v=None
while v==None:
    v = readint("Enter a number from -10 to 10: ", -10, 10)



print("The number is:", v)
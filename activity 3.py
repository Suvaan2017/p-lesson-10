num = int(input("Enter a number: "))
t = num
numLen = 0
while t > 0:
    numLen = numLen + 1
    t = int(t/10)
    if numLen >=4:
        chk = 0
        while num > 0:
            rem = num % 10
            if chk==numLen:
                midOne = rem
                elif chk==(numLen-1):
                midTwo = rem
                prod = midOne * midTwo
                print("\nThe product of the middle two digits is", prod)
            else:
                print ("\n It's not a 4 or more than 4-digit number")
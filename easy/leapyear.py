# Python program to check if year is a leap year or not

year = int(input("Enter a year"))

if (year % 4 ==0) and (year % 100 != 0): #year divided by 4 is leap year
    print("{0} is a leap year".format(year))

else:
    print("{0} is not a leap year".format(year))

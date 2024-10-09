year=2000
if(year%400==0)and(year%100==0):
    print("the year is leap year".format(year))
elif(year%4==0)and(year!=0):
    print("the year is leap".format(year))
else:
    print("the year is not a leapyear".format(year))
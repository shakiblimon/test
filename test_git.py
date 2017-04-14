print (" >>> This is test code for git <<< ")

year = int(input("Enter the Year: "))

if(year)%400 == 0:
    print("This is leap year")
elif (year)%4 == 0:
    print("This year is leap year ")
elif (year)%100 == 0:
    print("THis is leap year ")
else:
    print("This is not leap year")

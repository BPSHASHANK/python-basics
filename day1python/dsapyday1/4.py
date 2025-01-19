# find whether the year leap year or not
year=int(input("enter the year to check whether the year leap year or not"))
if year%400==0 or(year%4==0 and year%100!=0):
    print(f'the given year is {year} is an leap year')
else:
    print("not leap year")
    
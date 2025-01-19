# write a program for ticket picker which give $2 offer for the wednesday andfor <12 year child price will be 8else 10
age=(int(input("enter the age of the movie viewer \n")))
day="wednesday"
price=10 if age>12 else 8
if day=="wednesday":
    price-=2
    print(f'your age is {age} and by including the all offer the price will be {price}') 

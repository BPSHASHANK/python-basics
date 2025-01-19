# write a program to segrigate the age group eg<13,>13 19 teen>20adult>60 senior


age=int(input("enter the age of a person \n"))
if(age<13):
    print("child")
elif(age<20):
    print("teen")
elif(age<60):
    print("adult")
elif(age>60):
    print("senior")

# calculate the grade of the students if marks>90 A mark>80 B >70 C >60 D <50 f

mark=int(input("enter the marks of the student \n"))
if(mark>100):
    print("marks should less then 100")
elif(mark>90):
    print(f'your mark is {mark } your grade is "A"')
elif(mark>80):
    print(f'your mark is {mark } your grade is "B"')
elif(mark>70):
    print(f'your mark is {mark } your grade is "C"') 
elif(mark>60):
    print(f'your mark is {mark } your grade is "D"') 
elif(mark>50):
    print(f'your mark is {mark } your grade is "E"')          
elif(mark<50):
    print(f'your mark is {mark } your grade is "F"')
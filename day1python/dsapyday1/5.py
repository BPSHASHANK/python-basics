# count the positive number in an list
# mylsist=[1,3,4,5,6,-7,6,-4]
mylsist=[1,3,4,5,6,-7,6,-4]
count=0
for i in mylsist:
    if i>1:
        count+=1
        print(count)

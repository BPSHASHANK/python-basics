# calcuate the su of the even number
num=int(input("enter the number to find the sum of the even number"))
count=0
for i in range(1,num+1):
    if num%2==0:
        count+=i
        print(count)
        
#note in variable it do not hold any data type mean wnile 

#the address of the variable it holds data type
a=3
a="shashank"
#in an abobe example a=3 will replaced with a "shashank" 3 will go to garbage collection
#a is not number tyoe but 3a=3 3 become number type
#again a is not a string  but  "shashank" is number type


a=5
b=2
print(a)
print(b)
a=a+2
print(a)
#lets discuss about list
l1=[1,2,3]
l2=l1
print(l1)
print(l2)
#lets assign 0 th position of l1 be 44
l1[0]=22
print(l1)
#if we see this example the l2 have the reference of the l1
#because there is no other ref 
print(l2)



p1=[1,2,3]
p2=p1
p2=[1,2,3]
p1[0]=33
print(p1)
print(p2)


#while some condition we need to fouus on some things
h1=[1,2,3]
h2=h1[:]
h1[0]=33
print(h1)
print(h2)
#number

x=10
y=12
z=x+y
print(z)


#string
#string are nothing but which enclose with ""
username="shashank"
print(len(username))
#always start from 0 position
print(username[1])
#if we give the index of -1 it will starts from last
print(username[-1])
print(username[1:4])
dir(username)


#list :-list is specified by [] in list wecan add multiple type

mylist=[123,'chai','cofee']
print(len(mylist))
#list also have further steps as we discuss abouve



#dictionary
mydict={
    'name':"shashank",
    'age':23,
    'email':"shashanklkfsdjfdf@gmail.com"
}

print(mydict)
print(mydict['email'])

#touples which starts whth () 
mytup=(1,2,3,4)
print(mytup)
print(len(mytup))
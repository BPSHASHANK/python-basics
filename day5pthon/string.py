#lets discuss about the string
morining="very cool"
print(f"morning was{morining} ")
#we can add several method

firstchar=morining[1]
print(firstchar)
slice_method=morining[0:4]
print(slice_method)
list="0123456789"
print(list[:])
print(list[1:3])
print(list[0:8:2])
print(list[0:8:-2])
#string methods
#upper
print(morining.upper())
#lower case
print(morining.lower())
data="     shashank     "
#strip method is  used for the remove the space between the space
print(data.strip())
#replcace
print(morining.replace("very cool","its cool"))


#keep note this
chai="lemon,green,mint,ginger"
print(chai)
print(chai.split())
print(chai.split(" ,"))
#to find somthing in an python
print(chai.find("mint"))
newdata="chai chai chai chai cahi"
#count method is used for the count the total 
print(newdata.count("chai"))
#to declare a place holder

chai_type="mint"
quantity=3
order="i orderd {} cups of {} chai"
print(order.format(chai_type,quantity))
chai_types=["lemon","jinger","masala","mint"]
print("-".join(chai_types))
print(len(chai_types))
for letter in chai_types:
    print(letter) 
    #note if we want to print some thing like 
    chai1="he said,\"masala chai is awsome\""
    print(chai1)
    #in widows if we use lie this it gonna cause path problem so we need o use based on particular problem
    
    chai1=r"masala\nchai"
    print(chai1)
    
    
    #in some interview ask like in chai1 masala is there or not
    #solution
    print("masala"in chai1)
    
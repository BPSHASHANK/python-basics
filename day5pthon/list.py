 #list
chai_varities=["black_tea","Green_tea","White_tea"]
print(chai_varities)
#some opertions on lists
print(chai_varities[2])
print(chai_varities[:2])
#change "white tea " to hrebal tea
chai_varities[2]="herbal_chai"
print(chai_varities)
#keep note
#if we use like this it will give space and ,
chai_varities[1:2]="orange_tea"
print(chai_varities)
#to over come this we need to give 
chai_varities=["black_tea","Green_tea","White_tea"]
print(chai_varities)
chai_varities[1:2]=["lemon_tea"]
print(chai_varities)
#to add like


'''for tea in chai_varities:
    print(tea)
    for tea1 in chai_varities:
        print(tea1,end="-") '''
        
        #if condition
if "harbal" in chai_varities:
            print("i have herbal tea in list")
            chai_varities.append("harbal")
            print(chai_varities)
            if "harbal" in chai_varities:
                print("yes")
                
                chai_varities.insert(1,"madka")
                print(chai_varities)
            

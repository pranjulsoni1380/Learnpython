
name = input(" Enter Your Name : ")
temp ="" 

for i in range(len(name)):
    if name [i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
        temp += name[i]
        

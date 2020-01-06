number = input("Enter Your Four Digit Number : ")

total = 0
# i = 0

# while i <len(number):
#     total+= int(number[i])
#     i += 1
# print(total)

for i in number:
    total += int(i)
    
print(total)
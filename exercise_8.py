user_input = input("Enter Your Name : ")
i = 0
temp = ""

while i < len(user_input):
       if user_input[i] not in temp:
            temp += user_input[i]
            print(f"{user_input[i]} : {user_input.count(user_input[i])}")
            
       i += 1 
       
#     #  total =+ 1


# # a = "sonsdfsi" 
# # a = a.count("s") 
# # print(a)
# # print(total)



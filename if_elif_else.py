age = input("Enter Your age: ")
age = int(age)

if 2<age<=3:
    print("Ticket Price : Free")
elif 3<age<=10:
    print("Ticket Price : 150")
elif 10<age<60:
    print("Ticket Price : 250")
else:
    print("Sorry")


num = int(input("Guess a number between 0 to 100 : "))
temp = 1


for i in range(num):
    
    if num < 55:
        print('too low')
        break
    elif num > 55:
        print('too high')
        break
    elif num == 55:
        print("you Win")
        break
    

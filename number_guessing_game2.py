import random 
winning_number = random.randint(1,100)
guess = 1
num = int(input(" Enter any number : "))
game_over = False

while not game_over:
    if num == winning_number:
        print(f"You Win, and You Guessed this number in {guess} times")
        game_over = True
    else:   
        if num < winning_number:
            print("Too Low")
        
        else:
             print("Too High")
        guess += 1   
        num = int(input("Guess Again : "))
             
             # Dry - don't repeat yourself
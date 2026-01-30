import random 
user_wins = 0 
computer_win = 0 

while True: 
    user_input = input("Type Rock/ paper/scissor or Q to quit: ").lower()
    if user_input =="q":
        quit()
    

    if user_input in ["rock", "paper", "scissor"]: 
        print(f"you got it {user_input}")
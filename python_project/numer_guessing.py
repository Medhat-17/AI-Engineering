
import random #import modile 
import time
guesses=0

top_of_range  = input("Type a number: ")
if top_of_range.isdigit(): 
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print("please Enter a number larger than zero!")
        quit_msg = "Quitting cuz the number is less than zoer!" 
        for text_msg in quit_msg: 
            time.sleep(0.1)
            print(text_msg, end="", flush=True)
else:
    print("please type a number next time.")
    quit()
    

random_number = random.randint(0, top_of_range) 

while not False:
    guesses+=1
    user_guess = input("MAke a guess :")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number net time")
        continue 
    
    if user_guess==random_number:
        #simulate slow text
        msg= "you got it"
        print(msg)
        break
    else:
        print("you got it wrong? ")

print(f"you got it ijn {guesses}")
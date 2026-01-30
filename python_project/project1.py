#buildign a quiz game in python is really cool 
"""
Building a Quiz game is really easy 
"""
import time
from time import sleep
from tkinter import N
welocme = "welcome to hte quiz gmae bro!"
for text in welocme: 
    time.sleep(0.02)
    print(text, end="", flush=True)

score=0 #incemrenting score
user_play = input("Do you want to play? ")
if user_play.lower() != "yes": 
    #simulate qutiing 
    quit_text = "We are so sad you can't play htis gmae? "
    for msg in quit_text:
        time.sleep(0.2)
        print(msg, end="", flush=True)

print("let play this gmae? ")
q1= input("what is CPU stand for? ")
if q1.lower() =="central processing unit": 
    print("correct!")
    score+=1 #1 marks.
else:
    print("Incorrect!")

q2= input("what is GPU stand for? ")
if q2.lower() =="general processing unit": 
    print("correct!")
    score+=1 #1 marks.
else:
    print("Incorrect!")
    

q3= input("what is MPU stand for? ")
if q3.lower() =="Multi processing unit": 
    print("correct!")
    score+=1 #1 marks.
else:
    print("Incorrect!")
    

print(f"you got {score} " + "question correct!")
print(f" you got {score/4*100}", "%")



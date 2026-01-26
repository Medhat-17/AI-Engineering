marks = 0 

print("welcome to the quiz Game".capitalize())


q1 = input("what the capital of Russia  ? ").lower().strip() 
if q1 == "moscow": 
    print(f" your answer is correct {q1}") 
    marks+=1
    print(f"you got {marks}")
else:
    print("your are wrong!")


q2 = input("what is the capital of Pakistan? ").lower().strip()
if q2 =="islamabad": 
    marks+=1
    print(f"you got {marks}")
else:
    print("you are worng") 

q3= input("what is capital of Japan? ").lower().strip()

if q3=="tokyo":
    print("your are correct!")
    marks+=1
    print("your are reall good to greaT!")
else:
    print("you are wrong! ❌")


print(f"total marks you got out of {marks}")


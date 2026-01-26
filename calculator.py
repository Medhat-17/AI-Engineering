
import math 
while True: 
    
    print("1.Basic operations ")
    print("2. complicated Math")
    print("3.FActorial and other advanced calculator! ")

   

    user_choice = input("Enter 1-3 :")
    if user_choice=="exit": 
        break
    
    
    if user_choice=="1": 
        print("okay welcome to basic operations i nPYthon ")
        operatr_slection = input("select operators +, -, /, **, or type 'exit' to quit okay " ).lower() 
        if operatr_slection=="exit": 
            print("bye bye !")
            break

        elif operatr_slection=="+": 
            number1 = int(input("enter number 1: "))
            number2 = int(input("enter number 2: "))
            print(f" the sum of {number1} & {number2} is {number1+number2}")
        elif operatr_slection=="-": 
            number1 = int(input("enter number 1: "))
            number2 = int(input("enter number 2: "))
            print(f" the sum of {number1} & {number2} is {number1-number2}")
        elif operatr_slection=="/": 
            number1 = int(input("enter number 1: "))
            number2 = int(input("enter number 2: "))
            print(f" the sum of {number1} & {number2} is {number1/number2}") 
        elif operatr_slection=="*": 
            number1 = int(input("enter number 1: "))
            number2 = int(input("enter number 2: "))
            print(f" the sum of {number1} & {number2} is {number1*number2}") 
        
    if user_choice=="2": 
        print("welcome to complicated MAth")
        print("it includes stuff like math functions ")
        """" it includes stuff like sqrt and 
        maht libraries shit"""
        user_input =  input("type name of Function for example 'factorial' ").lower().strip()#easier
        if user_input=="factorial": 
            user_input_number = int(input("enter your number: "))
            print(math.factorial(user_input_number))
        elif user_input=="sqrt":
         user_input_number = int(input("enter your number: "))
         print(math.sqrt(user_input_number))

        elif user_input=="degrees": 
            degree_number = int(input("enter degree: "))
            print(math.cos(degree_number)) 

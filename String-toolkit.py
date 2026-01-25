#string toolkit aapp 
print("1. Uppercase")
print("2.Length of given text")
print("3.lower Case")
print("4.String reverasl")

user_input_2 = input("Enter number 1-5: ")
if user_input_2=="1": 
    sentence = input("enter sentence or something to make it uppecase? ")
    print(sentence.upper())
elif user_input_2=="2": 
    sentence = input('enter sentence to finds its length: ')
    print(len(sentence))
elif user_input_2=="3": 
    sentence = input("enter to covnert it to lower case: ")
    print(sentence.lower())
elif user_input_2=="4": 
    sentence = input("enter to covnert it to make it reversal case: ")
    print(sentence[::-1])

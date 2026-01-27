import time
#understanding slow-text effect.py

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

list_data = ["medhat", "data"]
user_input = input("Enter your favorite guy? ").lower().strip()

if user_input in list_data:
    slow_print("You got it right.. 🎉", 0.05)
else:
    slow_print("Oops! That’s not correct 😅", 0.05)

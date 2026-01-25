

import os 
import webbrowser #default url 

while not False: 
    choice = input("Enter app or URL to open it ").lower()
    if choice=="exit": 
        break 
    elif choice =="calc": 
        calculator = "okay opening clacaultro bro"
        calling_calc = os.system("calc")
        print(f"{calculator} nad yah {calling_calc}")#openign calcing 
    elif choice == "notepad": 
        #opeing notepad
        notepad = "okay openign notepad" 
        caling_notepad = os.system("notepad")
        print(f" {notepad} & {caling_notepad}")

    elif choice == "url": 
        url = input("Enter URL ").lower()
        webbrowser.open(url)#open url 
        print(f" your {url} is opening ")

else: 
    print("tpye randomg shit !")

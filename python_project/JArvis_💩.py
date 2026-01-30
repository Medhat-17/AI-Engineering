import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import math
"""

VOicenengine below"""
engine = pyttsx3.init('sapi5')  # Microsoft speech engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 = male, 1 = female
engine.setProperty('rate', 150)  # speaking speed

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ---------------- Greetings ---------------- #
def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis, your personal assistant. How can I help you today?")

# ---------------- Take Voice Command ---------------- #
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

# ---------------- Task Functions ---------------- #
def open_website(name):
    websites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "facebook": "https://www.facebook.com",
        "github": "https://www.github.com"
    }
    if name in websites:
        speak(f"Opening {name}")
        webbrowser.open(websites[name])
    else:
        speak(f"I am searching {name} on Google")
        webbrowser.open(f"https://www.google.com/search?q={name}")

def tell_time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {strTime}")

def tell_date():
    strDate = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {strDate}")

def search_wikipedia(query):
    speak("Searching Wikipedia...")
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    except Exception as e:
        speak("Sorry, I could not find any results.")

def open_app(app_name):
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe"
    }
    if app_name in apps:
        speak(f"Opening {app_name}")
        os.startfile(apps[app_name])
    else:
        speak(f"Sorry, I cannot find {app_name} on your system.")

def do_math(query):
    # Simple math eval (only safe operators)
    try:
        result = eval(query)
        speak(f"The answer is {result}")
    except:
        speak("I cannot calculate that.")

# ---------------- Main Jarvis ---------------- #
def run_jarvis():
    wish_user()
    while True:
        query = take_command()

        if "time" in query:
            tell_time()
        elif "date" in query:
            tell_date()
        elif "wikipedia" in query:
            query = query.replace("wikipedia", "")
            search_wikipedia(query)
        elif "open" in query:
            query = query.replace("open ", "")
            open_website(query)
        elif "launch" in query or "run" in query:
            query = query.replace("launch ", "").replace("run ", "")
            open_app(query)
        elif "calculate" in query or "what is" in query:
            query = query.replace("calculate", "").replace("what is", "")
            do_math(query)
        elif "exit" in query or "quit" in query or "goodbye" in query:
            speak("Goodbye! Have a nice day!")
            break
        elif query != "none":
            # Default: Google search
            open_website(query)

# ---------------- Start Jarvis ---------------- #
if __name__ == "__main__":
    run_jarvis()

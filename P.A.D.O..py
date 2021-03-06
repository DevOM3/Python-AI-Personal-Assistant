import pyttsx3
from googletrans import Translator
import pyaudio
import speech_recognition as sr
import pyspeech
import datetime
import wikipedia
import webbrowser
import os
import sys
import random
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def good():
    hour = datetime.datetime.now().hour
    # x = datetime.datetime.now().date()
    if hour > 00 and hour < 12:
        speak("Good Morning ")
    elif hour > 12 and hour < 17:
        speak("Good Afternoon")
    elif hour > 17 and hour < 19:
        speak("Good Evening")
    else:
        speak("Good Night")


def order():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm Listening ........")
        # rec.break_threshhold =1
        rec.adjust_for_ambient_noise(source)
        speak("I'm listening")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio,language='en-in')
        print("\n{}".format(text, dest='en'))
        # speak("Sir , you said "+r.recognize_google(audio))

    except Exception:
        print("Say it again please")
        speak("Say it again please")
        return "None"
    return text

# def name():
#     r=sr.Recognizer()
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source)
#         speak("What's your Name ?")
#         aud=r.listen(source)
#         nm=r.recognize_google(aud)
#         print(nm)
#     return nm


def done():
    sys.exit()


if __name__ == "__main__":
    good()
    # n=name()
    speak(f"Hello . I am PADO , your Personal Assistant")
    speak("Order me anything you want to do ...............")
    while 'True':
        text = order().lower()

        if 'wikipedia about' in text:
            result = wikipedia.summary(text, sentences=4)
            speak("According to web Results ")
            print(result)
            speak(result)

        elif text == 'open youtube':
            speak("Opening YouTube")
            webbrowser.open_new_tab("https://www.youtube.com/")

        elif text == 'open whatsapp':
            speak("Opening What's App")
            webbrowser.open_new_tab("https://web.whatsapp.com/")

        elif text == 'open google':
            speak("Opening Google")
            webbrowser.open_new_tab("https://www.google.co.in/")

        elif text == 'open instagram':
            speak("Opening Instagram")
            webbrowser.open_new_tab("https://www.instagram.com/?hl=en")

        elif text == 'open facebook':
            speak("Opening Facebook")
            webbrowser.open_new_tab("https://www.facebook.com/")

        elif text == 'open translator':
            speak("Opening Google Translator")
            webbrowser.open_new_tab("https://translate.google.co.in/")

        elif 'search on web' in text:
            print("Searching.........")
            speak("Searching.........")
            webbrowser.open_new_tab(text)

        elif text == 'exit':
            print("Okay , Sir . I am logging Off")
            print("Bye ! Have a nice day!!!")
            speak("Okay , Sir . I am logging Off")
            speak("Bye ! Have a nice day!!!")
            sys.exit()

        elif text == 'shutdown':
            speak("Shutting the PC")
            os.system("shutdown /s /t 1")

        elif text == 'restart':
            speak("Restarting")
            os.system("shutdown /s /t 1")

        elif 'date' in text:
            d = datetime.datetime.now().date()
            speak(d)
            print(d)

        elif text == 'open oracle':
            os.startfile("C:\\oraclexe\\app\\oracle\\product\\10.2.0\\server\\Database_homepage.url")

        elif text == 'open android studio':
            os.startfile("C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe")

        elif text == 'open firefox':
            os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

        elif text == 'open vs code':
            os.startfile("C:\\Users\\ompra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif text == 'open turbo c++':
            os.startfile("C:\\TURBOC3\\Turbo C++")

        elif text == 'open github':
            os.startfile("C:\\Users\\ompra\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe")

        elif text == 'open pycharm':
            os.startfile("C:\\Program Files\\JetBrains\\python\\bin\\pycharm64.exe")

        elif text == 'open chrome':
            os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        elif 'time' in text:
            now = datetime.datetime.now()
            t = now.strftime("%H:%M")

            speak(t)
            print(t)

        elif text == 'hi' or text == 'hello' or text == 'namaste':
            r = random.randrange(1, 5)
            if r == 1:
                speak("Namaste , Sir")
            if r == 2:
                speak("Hello , Sir")
            if r == 3:
                speak("Hi , Sir")
            if r == 4:
                speak("Raam Raam ")

        elif 'what is your name' in text:
            speak("I am PADO (A personal Assistant developed by Oam)")

        elif text == 'open calculator' or text == 'open calc':
            speak("Opening calculator.....")
            os.system("calc.exe")

        elif text == 'open camera':
            speak("Opening camera")
            os.system("cam.exe")

        elif text == 'open notepad':
            speak("Opening notepad")
            os.system("C:\\Windows\\System32\\notepad.exe")

        # elif text=='what is my name':
        #     speak(f"You just told me that my name is {n} . Is that right or you wanna change it ?")
        #     print(f"You just told me that my name is {n} . Is that right or you wanna change it ?")
        #     text=order().lower()
        #     if 'change' in text:
        #         n=name()
        #         speak(f"Okay , your name is updated as {n}")
        #         print(f"Okay , your name is updated as {n}")
        #     else:
        #         speak("Okay")
        #         print("Okay")

        elif text == 'play music':
            playlist = ["C:\\Users\\ompra\\Music\\Luis Fonsi - Despacito ft. Daddy Yankee(M4A_128K).m4a",
                        "C:\\Users\\ompra\\Music\\Ed Sheeran - Shape of You [Official Video](M4A_128K).m4a",
                        "C:\\Users\\ompra\\Music\\DJ Snake - Let Me Love You ft. Justin Bieber(M4A_128K).m4a",
                        "C:\\Users\\ompra\\Music\\DJ Snake - Taki Taki ft. Selena Gomez_ Ozuna_ Card(M4A_128K).m4a",
                        "C:\\Users\\ompra\\Music\\ZERO_ Mere Naam Tu Full Song _ Shah Rukh Khan_ Anu(M4A_128K).m4a",
                        "C:\\Users\\ompra\\Music\\Yo Yo Honey Singh_ MAKHNA Video Song _ Neha Kakkar(M4A_128K).m4a",
                        "C:\\Users\\ompra\\Music\\Apna Time Aayega _ Gully Boy _ Ranveer Singh _ Ali(M4A_128K).m4a",
                        "C:\\Users\\ompra\\Music\\The Chainsmokers - Closer ft. Halsey (Official Lyr(M4A_128K).m4a"]
            speak("Playing music.....")
            i = 0
            while i < 8:
                webbrowser.open(playlist[i])
                time.sleep(240)
                i += 1
            done()

        else:
            webbrowser.open_new_tab(text)

input()

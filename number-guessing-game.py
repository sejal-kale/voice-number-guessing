import random
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from tkinter import *


n=random.randint(1,100)
guess =1
print("Enter number from 1 to 100 : ")

# speak("tell the number")
# takecommand()  

def display():
    root=Tk()
    root.title("NUMBER-GUESSING-Game")
    root.geometry("644x344")
    l=Label(text="THANK YOU FOR PLAYING GAME..!",bg="yellow",fg="red",padx=1500,font="comicsansms 22 bold")
    l.pack(side=BOTTOM,padx=34)
    photo=PhotoImage(file ="congo.gif" ,format="gif -index 2")
    l =Label(image=photo)
    l.pack()

    root.mainloop()


print()
engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

# print(voices[0].id)



engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said:{query}\n')

    except Exception:
        # print(e)
        print('Say that again')
        return 'none'
    return query

while guess<11:
   
    
    print("Guess the number")
    speak("Guess the number")
    # takecommand() 
    a=takecommand()
    a=int(a)

    # a=int(input("guess the number : "))
    if a==n:
        display()

        print(f"You Have Won in {guess} guesses\n Thank You So Much For playing number guessing  game")
        speak(f"You Have Won in {guess} guesses\n Thank You So Much For playing number guessing  game")
        break
    elif a>n:
        print("You Have Entered Greater Number  ")
        speak("You Have Entered Greater Number  ")
    else:
        print("You Have Entered Smaller Number ")
        speak("You Have Entered Smaller Number ")

    print(f"Remaining guesses is {10 - guess}\n")
    speak(f"Remaining guesses is {10 - guess}\n")
    guess+=1

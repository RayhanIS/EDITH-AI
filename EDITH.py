import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good morning sir i am virtual assistent EDITH!Please tell me how may I help you")
    elif hour>=12 and hour<18:
        speak("good afternoon sir i am virtual assistent EDITH!Please tell me how may I help you") 
    else:
        speak("good night sir i am virtual assistent EDITH!Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mdraihanbd76@gmail.com', 'rayhanbd')
    server.sendmail('mdraihanbd76@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query or "open video online" in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")
        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("opening google")
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail")
        elif 'good bye' in query:
            speak("good bye")
            exit()
        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')
        elif 'who make you' in query or 'who created you' in query or 'who develop you' in query:
            ans_m = " For your information Rayhan Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)
        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Jarvis an A I based computer program"
            print(about)
            speak(about)
        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
            ex_exit = 'exiting AI'
            speak(ex_exit)
            exit()
        elif 'open browser' in query:
            browserPath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            os.startfile(browserPath)
        elif 'open g' in query:
            gamelooppath = "F:\TxGameAssistant\AppMarket\AppMarket.exe"
            os.startfile(gamelooppath)
        elif 'email to abbu' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mdfaishalbd76@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")
                                                                              
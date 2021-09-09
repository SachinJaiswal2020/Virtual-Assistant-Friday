import pyttsx3
import speech_recognition as sr 
import datetime
import webbrowser
import pyautogui
import os
import smtplib
import random
import pywhatkit as kit
import pyjokes
import requests

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Friday sir, Please tell me how may i help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration =1)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        return "This mail was send by F.R.I.D.A.Y"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your Email', 'Email's Password')
    server.sendmail('Your Email', to, content)
    server.close()

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=c58cb113c28d40fc95442c7d962b6abd'

    main_page = requests.get(main_url).json()

    articles = main_page["articles"]
    head = []
    day=["first","second","third","fourth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        print(f"{head[i]}")
        speak(f"today's{day[i]} news is: {head[i]}")

def screenshot():
    img = pyautogui.screenshot()
    img.save('D:/python/screenshot.png')

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open notepad' in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'open google' in query:
            speak("sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open over' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'open insta' in query:
            webbrowser.open("instagram.com") 

        elif 'take screenshot' in query:
            speak("taking screenshot")
            screenshot() 

        elif 'open command' in query:
            os.system("start cmd")

        elif "sleep" in query:
            speak("Have a Good Day, peace")
            quit()

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif "message" in query:
            kit.sendwhatmsg("Receivers Number", "Message you want to send",hour,min)

        elif "play song on youtube" in query:
            kit.playonyt("franchise travis scott")

        elif "latest news" in query:
            speak("please wait sir, fetching the latest news")
            news()

        elif 'play music' in query:
            music_dir = 'Folder Location Of Song's'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)   
            os.startfile(os.path.join(music_dir, rd))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Receivers Email"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend sachin. I am not able to send this email")    

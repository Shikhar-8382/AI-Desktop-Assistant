import pyaudio # THIS IS THE LIBRARY YOU NEED TO INSTALL FIRST
import pyautogui
import pyttsx3
import datetime
from datetime import date
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import pywhatkit
import requests
from bs4 import BeautifulSoup
import subprocess


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

# SPEAK FUNCTION
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# WISH ME FUNCTION THIS FUNCTION WISH GREETINGS LIKE - GOOD MORNING, GOOD NIGHT etc.
def wishMe():
    speak("I am online activated sir ")

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Night Sir")

    print("Initializing......")
    speak("How can I help you today")

# THIS FUNCTION LISTEN THE VOICE COMMANDS
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hearing......")
        r.pause_threshold = 1
        audio = r.listen(source,0,3)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"ME : {query}\n")

    except Exception as e:
        #print(e)
        print("Please say again sir.....")
        speak("Please say again sir.....")
        return "None"
    return query


# THIS FUNCTION SEND EMAIL - JUST INSERT YOUR E-MAIL ID AND SENDER's EMAIL-ID

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(# Your E-mail ID )
    server.sendmail((# Your E-mail ID)
    server.close()

# THIS FUNCTION SEND MESSAGE ON WHATSAPP JUST INSERT THE PH-NUMBER
def sendWhatappMessage(human, message,):
   # hour = int(datetime.datetime.now().strftime("%H"))-10
   # minutes = int(datetime.datetime.now().strftime("%M"))-10
    pywhatkit.sendwhatmsg_instantly(human, message)

# THIS IS THE MAIN FUNCTION ALL EXECUTION PART STARTS FROM HERE :::::::::::

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            query = query.replace("wikipedia", " ")
            result = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia sir")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'close youtube' in query:
            subprocess.call("TASKKILL /F /IM msedge.exe", shell=True)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'close google' in query:
            subprocess.call("TASKKILL /F /IM msedge.exe", shell=True)

        elif 'open youtube music' in query:
            webbrowser.open("music.youtube.com")

        elif 'close youtube music' in query:
            subprocess.call("TASKKILL /F /IM msedge.exe", shell=True)

        elif 'open my website' in query:
            webbrowser.open("https://shikharlogics.github.io/myWebsite/")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'close stack overflow' in query:
            subprocess.call("TASKKILL /F /IM msedge.exe", shell=True)

        elif 'play my song playlist' in query:
            music_dir = "C:\\Users\\HP\\OneDrive\\Desktop\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            song_random = random.randrange(-1,7)
            os.startfile(os.path.join(music_dir, songs[song_random]))

        elif 'close my song playlist' in query:
            subprocess.call("TASKKILL /F /IM vlc.exe", shell=True)

        elif ' tell me time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            speak(f"Sir, the time is{time}")

        elif 'tell me today date' in query:
            date = datetime.datetime.now().strftime("%D")
            print(date)
            speak(f"Sir, the date is{date}")

        elif 'weekday today' in query:
            week = date.today()
            if week.weekday() == 0:
                print("MONDAY")
                speak("Today is Monday")
            elif week.weekday() == 1:
                print("TUESDAY")
                speak("Today is Tuesday")
            elif week.weekday() == 2:
                print("WEDNESDAY")
                speak("Today is Wednesday")
            elif week.weekday() == 3:
                print("THURSDAY")
                speak("Today is Thursday")
            elif week.weekday() == 4:
                print("FRIDAY")
                speak("Today is Friday")
            elif week.weekday() == 5:
                print("SATURDAY")
                speak("Today is Saturday")
            else:
                print("SUNDAY")
                speak("Today is Sunday")

        elif 'open code idea' in query:
            minePath = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2023.2\\bin\\idea64.exe"
            print("opening Intellij idea.....")
            speak("opening Intellij idea")
            os.startfile(minePath)

        elif 'close code idea' in query:
            subprocess.call("TASKKILL /F /IM idea64.exe", shell=True)

        elif 'open vs code' in query:
            minePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            print("opening vs code.....")
            speak("opening vs code")
            os.startfile(minePath)

        elif 'close vs code' in query:
            subprocess.call("TASKKILL /F /IM Code.exe", shell=True)

        elif 'open github desktop' in query:
            minePath = "C:\\Users\\HP\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
            print("opening github.....")
            speak("opening github")
            os.startfile(minePath)

        elif 'close github' in query:
            subprocess.call("TASKKILL /F /IM GitHubDesktop.exe", shell=True)

        elif 'open notepad' in query:
            minePath = "C:\\Program Files\\Notepad++\\notepad++.exe"
            print("opening notepad.....")
            speak("opening notepad")
            os.startfile(minePath)

        elif 'close notepad' in query:
                subprocess.call("TASKKILL /F /IM notepad++.exe", shell=True)

        elif 'open photoshop' in query:
            minePath = "C:\\Program Files\\Adobe\\Adobe Photoshop 2023\\Photoshop.exe"
            print("opening adobe photoshop.....")
            speak("opening adobe photoshop")
            os.startfile(minePath)

        elif 'close Photoshop' in query:
                subprocess.call("TASKKILL /F /IM Photoshop.exe", shell=True)

        elif 'send email to my friend' in query:
            try:
                print("What message you want to send?")
                speak("What message you want to send")
                content = takeCommand()
                to = # Sender's E-Mail ID
                sendEmail(to, content)
                speak("Sir Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry sir, I cant send the Email")

        elif 'send message on whatsapp' in query:
            try:
                print("What message you want to send?")
                speak("What message you want to send")
                message = takeCommand()
                number = # Your Mobile Number or What's App Number

                sendWhatappMessage(number, message)
                speak("Message has been sent")
            except Exception as e:
                 print(e)
                 speak("Sorry Sir, Message not sent")

        elif 'tell me temperature' in query:
            print("Sir which city temperature you want to know?")
            speak("Sir which city temperature you want to know")
            search = takeCommand()
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            set = BeautifulSoup(r.text, "html.parser")
            temp = set.find("div", class_="BNeawe").text
            print(temp)
            speak(f"Sir {search} is {temp}")

        elif 'tell me battery power' in query:
            import psutil
            battery = psutil.sensors_battery()
            percent_Battery = battery.percent
            print(f"Sir our system have {percent_Battery} percent battery left")
            speak(f"Sir our system have {percent_Battery} percent battery left")
            if percent_Battery < 100 and percent_Battery > 75:
                speak("Enough battery to work sir")
            elif percent_Battery < 60  and percent_Battery > 40:
                speak("much battery sir to work")
            elif percent_Battery < 35 and percent_Battery > 15:
                speak("Sir please give me power")
            else:
                speak("I am dead in few minutes sir")

        elif 'volume up' in query:
            speak("Sure Sir")
            for i in  range(5):
                pyautogui.press("volumeup")
        elif 'volume down' in query:
            speak("Sure Sir")
            for i in range(5):
                pyautogui.press("volumedown")
        elif 'volume mute' in query:
            speak("Sure Sir")
            pyautogui.press("volumemute")


        elif 'exit' in query:
            speak("Exit command Sir, You can call me anytime sir")
            speak("bye bye sir")
            exit()

















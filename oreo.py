import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!Vipul")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!Vipul")   

    else:
        speak("Good Evening!Vipul")  

    speak("I am Mini! Please tell me how may I help you")       

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
        if 'Hii Mini' in query:
                query = query.replace('Hii Mini', '')
                print(query)

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'tell something about' in query:
            speak('Searching Wikipedia...')
            query = query.replace("tell something about", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open_new_tab("www.youtube.com")

        elif 'open whatsapp' in query:
            webbrowser.open_new_tab("https://web.whatsapp.com")

        elif 'open google' in query:
            webbrowser.open_new_tab("https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwieppfqiv_yAhXObSsKHV_nA54QPAgI")

        elif 'open stack overflow' in query:
            webbrowser.open_new_tab("www.stackoverflow.com")   


        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)   
            pywhatkit.playonyt(song)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Vipul\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open Command Prompt' in query:
            codePath = "C:\\Users\\Vipul\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.exe"
            os.startfile(codePath)

        elif 'open Cisco Packet Tracer' in query:
            codePath = "C:\\Program Files\\Cisco Packet Tracer 7.3.0\\bin\\PacketTracer7.exe"
            os.startfile(codePath)

        elif 'send mail to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vipulchaudhary2005@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Vipul! I am not able to send this email")

        elif 'date' in query:
            speak('sorry, I have a headache')

        elif 'are you single' in query:
            speak('I am in a relationship with wifi')

        elif 'thank you mini' in query:
            speak('your welcome vipul')
            exit()

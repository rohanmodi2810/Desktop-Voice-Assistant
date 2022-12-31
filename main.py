import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import pyjokes
import smtplib
import wolframalpha
from playsound import playsound
import requests
import datetime
import os
import random
import subprocess
import winshell

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

assname = "JARVIS"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=  0 and hour < 12:
        speak("Good Morning Sir!")
  
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")   
  
    else:
        speak("Good Evening Sir!")  
  
    speak(f"I am your assistant {assname}. Please tell me how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\nListening...")
        playsound("beep.mp3")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
  
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language ='en-in')
        print(f"\nUser said: {query}")
  
    except sr.UnknownValueError:
            print(f"\n{assname} said: I did not get that!")
            speak("Sorry! I did not get that.")
            return "None"
    
    except sr.RequestError:
            print(f"\n{assname} said: Please check your internet connection!")
            speak("Sorry, the internet connection is down.")
            return "None"
     
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login("r.c.m.modi2810@gmail.com", "Rohan3142")
    server.sendmail("r.c.m.modi2810@gmail.com", to, content)
    server.close()

def there_exists(terms, query):
    for term in terms:
        if term in query:
            return True

if __name__ == "__main__":
    os.system('cls')
    wishMe()

    while True:
        query = takeCommand().lower()

        # 1: questions
        if there_exists(["what is your name", "what's your name", "tell me your name"], query):
            print(f"{assname}")
            speak(f"My name is {assname}.")

        elif there_exists(["how are you", "how are you doing"], query):
            speak("I'm very well, thanks for asking.")
    
        elif there_exists(["who created you", "who is your creator", "who made you"], query):
            print("ROHAN MODI")
            speak("My creator is Rohan Modi.")

        elif there_exists(["who are you"], query):
            speak("I am your virtual voice assistant. I can perform simple tasks for you on this computer.")

        elif there_exists(["who i am"], query):
            speak("If you talk then definitely you are human")

        elif there_exists(["reason for you", "why were you created", "why you came"], query):
            speak("I was created as a minor project by Rohan.")
        
        elif there_exists(["thank you", "thanks"], query):
            speak("Your most welcome sir!")

        elif there_exists(["what do you know", "what can you do", "what can you perform"], query):
            speak("I can perform the following tasks :")
            print('''
            1. Greet you
            2. Answer basic questions
            3. Tell the current time
            4. Tell today's date
            5. Open VScode
            6. open simple websites like youtube.com, google.com, facebook.com, etc.
            7. Tell a joke
            8. Search keyword on Wikipedia
            9. Send an email
            10. Simple calculator
            11. Google search
            12. Tell latest news
            13. Search location on map
            14. Open camera
            15. Maintain notes
            16. Tell current weather
            17. Toss a coin
            18. Pause listening
            19. Empty recycle bin
            20. Lock, hibernate/sleep, restart or shutdown system
            ''')

        # 2: time
        elif there_exists(["what's the time", "tell me the time", "what time is it"], query):
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {time}")
        
        # 3: date
        elif there_exists(["what's the date", "tell me the date", "what date is it"], query):
            date = datetime.date.today().strftime("%d %B, %Y")
            speak(f"Today's date is {date}")

        # 4: open vscode
        elif there_exists(["open vs code"], query):
            path = "C:\\Users\\ROHAN MODI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        # 5: open websites
        elif there_exists(["open"], query):
            search_term = query.split()[-1]
            url = "https://" + str(search_term)
            webbrowser.get().open(url)
            speak("Here you go to " + search_term)

        # 6: tell a joke
        elif there_exists(["joke", "funny", "laugh"], query):
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        # 7: Wikipedia
        elif there_exists(["wikipedia", "definition of"], query):
            try:
                speak('searching wikipedia...')
                query = query.replace("wikipedia", "")
                query = query.replace("definition of", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to wikipedia")
                print(results)
                speak(results)
            
            except Exception as e:
                print(e)
                speak("Sorry! I am not able to receive information from wikipedia.")

        # 8: Send an email
        elif there_exists(["mail", "email"], query):
            try:
                speak("Please type whom should I send?")
                to = input("To:  ")
                speak("Please type what should I send?")
                content = input("Content:  ")
                sendEmail(to, content)
                speak("Email has been sent successfully!")
            
            except Exception as e:
                print(e)
                speak("Sorry! I am not able to send this email.")

        # 9: Calculator
        elif there_exists(["calculate"], query):
            try:
                app_id = "JLTHJU-G4LX8KAHR9"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)

            except Exception as e:
                print(e)
                speak("Sorry! I am not able to calculate this.")

        # 10: search google
        elif there_exists(["search"], query):
            search_term = query.replace("search", "")
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            speak("Here is what I found for" + search_term + "on google")

        # 11: News
        elif there_exists(["news"], query):
            try:
                api_key = "a0994c6c7fc84a37bf0bc98f4dae1869"
                url = f"https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey={api_key}"
                data = requests.get(url).json()

                speak("Here are some of the top news from the times of india")
                print('''============================ TIMES OF INDIA ============================\n''')
                i=1
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(e)
                speak("Sorry! I am not able to get the news.")

        # 12: location on map
        elif there_exists(["where is", "location of"], query):
            query = query.replace("where is", "")
            query = query.replace("location of", "")
            location = query
            speak(f"Here is the map of {location}")
            webbrowser.open("https://www.google.com/maps/place/" + location)

        # 13: Open camera
        elif there_exists(["take photo", "capture photo"], query):
            subprocess.run('start microsoft.windows.camera:', shell=True)

        # 14: Maintain Notes
        elif there_exists(["make a note", "write a note"], query):
            speak("What should I write sir?")
            note = takeCommand()
            with open("notes.txt", 'a') as file:
                time = datetime.datetime.now().strftime("%H:%M:%S")
                date = datetime.date.today().strftime("%d-%b-%Y")
                file.write(f"{date} | {time} | {note}" + "\n")
            speak("Note has been created successfully")

        elif there_exists(["show notes"], query):
            speak("showing notes")
            try:
                with open("notes.txt", 'r') as file:
                    notes = file.readlines()
                    print('''===================== YOUR NOTES =====================\n''')
                    for note in notes:
                        print(note)
            
            except FileNotFoundError:
                speak("You do not have any notes sir.")

        # 15: Weather
        elif there_exists(["weather"], query):
            api_key = "b44103fe8ca559e7bf0a13305bcb7e59"
            speak("Please tell city name")
            city_name = takeCommand()
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
            data = requests.get(url).json()
            print(data)

            if data["cod"] != '404':
                x = data["main"]
                curr_temperature = round(x["temp"] - 273.15, 2)
                description = data["weather"][0]["description"]
                report = f"Currently in {city_name} it is {curr_temperature} degree celsius with {description}."
                speak(report)
            else:
                speak("City not found!")
        
        # 16: toss a coin
        elif there_exists(["toss a coin", "flip a coin"], query):
            moves = ["heads", "tails"]
            choice = random.choice(moves)
            speak("The coin shows " + choice)

        # 17: pause listening
        elif there_exists(["pause listening", "stop listening"], query):
            print(f"{assname} said: Listening is paused.")
            speak("Listening is paused.")
            r2 = sr.Recognizer()
            while True:
                with sr.Microphone() as source2:
                    r2.pause_threshold = 1
                    r2.adjust_for_ambient_noise(source2)
                    audio2 = r2.listen(source2, timeout=None)
        
                try:
                    query2 = r2.recognize_google(audio2, language ='en-in')
                    if there_exists(["resume listening", "start listening"], query2):
                        speak("I am listening now.")
                        break
                    else:
                        continue
        
                except sr.UnknownValueError:
                    print(f"{assname} said: Listening is paused. Say 'resume listening' or 'start listening' to start listening.")
                    speak("Listening is paused. Say resume listening or start listening when you're ready.")
            
                except sr.RequestError:
                    print(f"{assname} said: Please check your internet connection!")
                    speak("Sorry, the internet connection is down.")

        # 18: empty recycle bin
        elif there_exists(["empty recycle bin"], query):
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle bin emptied successfully.")

        # 19: lock, hibernate, restart or shutdown system
        elif there_exists(["lock system"], query):
            speak("Locking system")
            subprocess.call('rundll32.exe user32.dll, LockWorkStation')
        
        elif there_exists(["hibernate system"], query):
            speak("Hibernating the system")
            subprocess.call(["shutdown", "/h"])

        elif there_exists(["restart system"], query):
            speak("Restarting system")
            subprocess.call(["shutdown", "/r"])
        
        elif there_exists(["shutdown system"], query):
            speak("Shutting down system")
            subprocess.call(["shutdown", "/s"])

        # 20: close
        elif there_exists(["quit", "goodbye", "bye", "exit"], query):
            speak("Goodbye, have a nice day sir!")
            exit()
        
        else:
            pass
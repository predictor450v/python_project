import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import time
import datetime

recognizer = sr.Recognizer()

def speak(text):
    # Initialize the engine inside the function
    engine = pyttsx3.init()
    
    # Set properties inside here too
    engine.setProperty('rate', 170)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) # Make sure this index [1] exists! for female voice
    
    # Speak
    engine.say(text)
    engine.runAndWait()
    engine.stop() # Force close the loop

def processCommand(c):   #command block for webpages
    if "google" in c.lower(): 
        wb.open("https://google.com")
    elif "youtube" in c.lower():
        wb.open("https://youtube.com")
    elif "chatgpt" in c.lower():
        wb.open("https://chatgpt.com/")
    elif "github" in c.lower():
        wb.open("https://github.com/predictor450v?tab=overview&from=2026-01-01&to=2026-01-12")
    elif "portfolio" in c.lower():
        wb.open("https://my-portfolio-bay-psi-99.vercel.app/")
    elif "gemini"or"geminai" in c.lower():
        wb.open("https://gemini.google.com/u/2/app?pageId=none")
    elif "time" in c:
        # New feature: Tells current time
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")





if __name__ == "__main__":
    speak("Initializing virtual assistant Friday")
    time.sleep(1)

    while True:
        print("Say 'Friday' to activate...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            
            word = recognizer.recognize_google(audio).lower()
            print(f"You said: {word}")
            
            if "friday" in word:
                print("Wake word detected!")
                speak("tell me")
                time.sleep(1)
                
                
            
                with sr.Microphone() as source:
                    print("jervis activeted...\ngive command...")
                    audio = recognizer.listen(source)
                    c = recognizer.recognize_google(audio).lower()
                    print(f"Command: {c}")
                
                
                # Process commands
                processCommand(c)
                
        except sr.UnknownValueError:
            pass # Silence is better than constant error printing
        except sr.RequestError as e:
            print(f"Network/API Error: {e}")
        except sr.WaitTimeoutError:
            pass
        except Exception as e:
            # Catch pyttsx3 errors specifically
            print(f"An error occurred: {e}")
    
    

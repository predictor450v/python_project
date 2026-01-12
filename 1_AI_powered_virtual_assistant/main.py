import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import time

recognizer = sr.Recognizer()

def speak(text):
    # Initialize the engine inside the function
    engine = pyttsx3.init()
    
    # Set properties inside here too
    engine.setProperty('rate', 170)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) # Make sure this index [1] exists!
    
    # Speak
    engine.say(text)
    engine.runAndWait()
    engine.stop() # Force close the loop

def processCommand(c):   #command block for webpages
    if "open google" in c.lower(): 
        wb.open("https://google.com")
    elif "open youtube" in c.lower():
        wb.open("https://youtube.com")
    
if __name__ == "__main__":
    speak("Initializing virtual assistant jarvis")
    time.sleep(1)

    while True:
        print("Say 'Jarvis' to activate...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            
            word = recognizer.recognize_google(audio).lower()
            print(f"You said: {word}")
            
            if "jarvis" in word:
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
    
    

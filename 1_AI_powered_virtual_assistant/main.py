import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import time
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


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
            time.sleep(0.5)  
            speak("how can i help you")
            time.sleep(0.5)  
        
            with sr.Microphone() as source:
                print("jervis activeted...")
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio).lower()
                print(f"Command: {command}")
            
            
            # Process commands
            
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Error: {e}")
    except sr.WaitTimeoutError:
        pass
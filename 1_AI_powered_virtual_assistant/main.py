import speech_recognition as sr
import webbrowser as wb
import pyttsx3

recognizer = sr.Recognizer()
recognizer.energy_threshold = 3000
recognizer.dynamic_energy_threshold = True

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  


def speak(text):
    engine.say(text)   
    engine.runAndWait()


if __name__ == "__main__":
    speak("Initializing virtual assistant jarvis")
    
    
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
                speak("how can i help you")
           
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
import speech_recognition as sr
import webbrowser as wb
import pyttsx3

recognizer = sr.Recognizer()
recognizer.energy_threshold = 3000
recognizer.dynamic_energy_threshold = True

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  


def speak(text):
    engine.say(text)   
    engine.runAndWait()

def processCommand():
    pass


if __name__ == "__main__":
    speak("Initializing virtual assistant jarvis")
    
    while True:
        print("Say 'Jarvis' to activate...")
        
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            
            word = recognizer.recognize_whisper(audio, model="base")
            print(f"You said: {word}")
            
            if "jarvis" in word.lower():
                speak("How can I help you master?")
           
                with sr.Microphone() as source:
                    print("Jarvis active - listening for command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                
                command = recognizer.recognize_whisper(audio, model="base").lower()
                print(f"Command: {command}")
                
                # Process commands
                processCommand()
                
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error: {e}")
        except sr.WaitTimeoutError:
            pass  # Silent timeout, just continue
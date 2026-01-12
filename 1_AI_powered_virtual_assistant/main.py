import speech_recognition as sr
import webbrowser as wb
import pyttsx3

recognizer =sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  


def speak(text):
    engine.say(text)
    
    engine.runAndWait()


if __name__== "__main__":
    speak("Initializing virtual assistant jarvis....")
    # wake word sara
    
    while True:
        # obtain audio from the microphone
        # recognize speech using Google
        r = sr.Recognizer()
       
        print("recogniging")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source ,timeout =1 ,phrase_time_limit=1)
            command =recognizer.recognize_google(audio).lower()
            print(command)
            if "jarvis" in command:
                speak("Yes, how can I help you?")


        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error: {e}")
        except sr.WaitTimeoutError:
            print("Listening timed out")


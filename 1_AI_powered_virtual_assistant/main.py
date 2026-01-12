import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import pocketsphinx

recognizer =sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  


def speak(text):
    engine.say(text)
    
    engine.runAndWait()


if __name__== "__main__":
    speak("Initializing virtual assistant Sara....")
    # wake word sara
    
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        # recognize speech using Sphinx
        try:
            command =recognizer.recognize_google(audio)
            print(command)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))


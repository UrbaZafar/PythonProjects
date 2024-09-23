import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

# initialize text speech engine
def speak(text):
    engine=pyttsx3.init() # initialize
    engine.say(text)
    engine.runAndWait() 

def listen():
    recognizer=sr.Recognizer() #creates an recognizr object 
    with sr.Microphone() as source: #use microphone as source for audio
        print("listening")
        audio=recognizer.listen(source) #records user voice

# if speech recognition is not working we can inform user that something went wrong with this message
        try:
            return recognizer.recognize_google(audio).lower()
        except:
            speak("sorry, cant understand")
            return None
def tell_time():
    time = datetime.datetime.now().strftime('%I:%M %p')  # Format the time (e.g., 11:30 AM)
    speak(f"The current time is {time}")

def telldate():
    date=datetime.datetime.now().strftime('%d,%B,%Y')
    speak(f"Today date is {date}")

def search_Web():
    speak("Opening")
    webbrowser.open(f"https://www.google.com/")


def respond(command):
    if "hello" in command:
        speak("Hello! How are you?")
    elif "your name" in command:
        speak("I am your assistant.")
    elif "i am hungry" in command:
        speak("I am not your mother, go away.")
    elif "time" in command:
        tell_time()
    elif "date" in command:
        tell_date()
    elif "search" in command:
        Opening()  # Opens Google homepage
    elif "what to do with my life" in command:
        speak("Sleep. Go sleep some more.")
    elif "bye" in command:
        speak("Goodbye! Shutting down now.")
        return False  # Signal to stop the assistant
    else:
        speak("What are you even saying?")
    return True

def main():
    while True:
        command = listen()
        if command:
            keep_running = respond(command)  # Get a signal if we should stop
            if not keep_running:
                break  # Exit the loop if "bye" is detected


if __name__ == "__main__":
    main()
import pyttsx3
import speech_recognition as sr
import datetime
# Initialize the speech engine
engine = pyttsx3.init()

# Set the speech rate
engine.setProperty('rate', 150)

# Set the speech volume
engine.setProperty('volume', 1.0)

# Define a function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to get user input via speech recognition
def get_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that. Please try again.")
            return get_user_input()

# Define a function to handle user queries
def handle_query(text):
    if "what time" in text:
        speak("The current time is " + datetime.datetime.now().strftime("%H:%M:%S"))
    elif "goodbye" in text:
        speak("Goodbye! Have a great day!")
        exit()
    else:
        speak("Sorry, I didn't understand that. Please try again.")

# Main loop
while True:
    user_input = get_user_input()
    handle_query(user_input)

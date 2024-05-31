import pyttsx3 
<Br>
import speech_recognition as sr
<Br>
import datetime
<Br>
# Initialize the speech engine
<Br>
engine = pyttsx3.init()
<Br>
# Set the speech rate
<Br>
engine.setProperty('rate', 150)
<Br>
# Set the speech volume
<Br>
engine.setProperty('volume', 1.0)

<Br>
# Define a function to speak text
<Br>
def speak(text):
   <Br>
   engine.say(text)
    <Br>
    engine.runAndWait()

<Br>
# Define a function to get user input via speech recognition
<Br>
def get_user_input():
   <Br>
   r = sr.Recognizer()
    <Br>
    with sr.Microphone() as source:
       <Br>
       print("Listening...")
        <Br>
        audio = r.listen(source)
        <Br>
        try:
           <Br>
           text = r.recognize_google(audio)
            <Br>
            return text
        <Br>
        except sr.UnknownValueError:
           <Br>
           speak("Sorry, I didn't understand that. Please try again.")
            <Br>
            return get_user_input()

<Br>
# Define a function to handle user queries
<Br>
def handle_query(text):
   <Br>
   if "what time" in text:
      <Br>
      speak("The current time is " + datetime.datetime.now().strftime("%H:%M:%S"))
    <Br>
    elif "goodbye" in text:
       <Br>
       speak("Goodbye! Have a great day!")
        <Br>
        exit()
    <Br>
    else:
       <Br>
       speak("Sorry, I didn't understand that. Please try again.")

<Br>
# Main loop
<Br>
while True:
   <Br> 
   user_input = get_user_input()
    <Br>
    
    handle_query(user_input)

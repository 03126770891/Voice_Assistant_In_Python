import pyttsx3 
<B>
import speech_recognition as sr
<B>
import datetime
<B>
# Initialize the speech engine
<B>
engine = pyttsx3.init()
<B>
# Set the speech rate
<B>
engine.setProperty('rate', 150)
<B>
# Set the speech volume
<B>
engine.setProperty('volume', 1.0)

<B>
# Define a function to speak text
<B>
def speak(text):
   <B>
   engine.say(text)
    <B>
    engine.runAndWait()

<B>
# Define a function to get user input via speech recognition
<B>
def get_user_input():
   <B>
   r = sr.Recognizer()
    <B>
    with sr.Microphone() as source:
       <B>
       print("Listening...")
        <B>
        audio = r.listen(source)
        <B>
        try:
           <B>
           text = r.recognize_google(audio)
            <B>
            return text
        <B>
        except sr.UnknownValueError:
           <B>
           speak("Sorry, I didn't understand that. Please try again.")
            <B>
            return get_user_input()

<B>
# Define a function to handle user queries
<B>
def handle_query(text):
   <B>
   if "what time" in text:
      <B>
      speak("The current time is " + datetime.datetime.now().strftime("%H:%M:%S"))
    <B>
    elif "goodbye" in text:
       <B>
       speak("Goodbye! Have a great day!")
        <B>
        exit()
    <B>
    else:
       <B>
       speak("Sorry, I didn't understand that. Please try again.")

<B>
# Main loop
<B>
while True:
   <B> 
   user_input = get_user_input()
    <B
    
    handle_query(user_input)

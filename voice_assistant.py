import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import tkinter as tk

# Initialize pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)  # 1 for female and 0 for male voice

root = tk.Tk()
root.title("Voice Assistant")

# Create labels
label = tk.Label(root, text="Voice Assistant", font=("Helvetica", 24))
label.pack(pady=20)

status_label = tk.Label(root, text="Listening...", font=("Helvetica", 16))
status_label.pack(pady=10)

# Define functions
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        status_label.config(text="Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        return query.lower()
    except Exception as e:
        print(e)
        speak("I didn't understand")
        return "None"

def process_query():
    query = take_command()
    if 'wikipedia' in query:
        status_label.config(text="Searching Wikipedia ...")
        query = query.replace("wikipedia", '')
        results = wikipedia.summary(query, sentences=2)
        status_label.config(text="According to Wikipedia:")
        speak("According to Wikipedia")
        speak(results)
    elif 'are you' in query:
        speak("I am amigo developed by Jaspreet Singh")
    # Add more command processing here...
    else:
        status_label.config(text="Command not recognized.")

def on_exit():
    root.destroy()

# Create buttons
search_button = tk.Button(root, text="Search", command=process_query, font=("Helvetica", 16))
search_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=on_exit, font=("Helvetica", 16))
exit_button.pack(pady=10)

root.mainloop()

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pygame
import pyjokes
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Buddy!")
        print("Good Morning Buddy!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Buddy!")
        print("Good Afternoon Buddy!")
    else:
        speak("Good Evening Buddy!")
        print("Good Evening Buddy!")
    speak("Hello, I am Aegis Sir, How may I help you")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognition..")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")
        return query.lower()
    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query


def tell_joke():
    joke = pyjokes.get_joke()  # Get a random joke
    speak(joke)
    print(joke)


if __name__ == '__main__':
    wish_me()
    while True:

        query = takeCommand()

        # logic for executing tasks based on the query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open yahoo' in query:
            webbrowser.open('yahoo.com')
        elif 'open google chrome' in query:
            webbrowser.open('google chrome.com')
        elif 'tell me a joke' in query:
            tell_joke()

        elif 'play music' in query:

            music_dir = 'F:\\music\\ENGLISH SONGS\\avril lavgine'
            pygame.mixer.init()
            songs = [file for file in os.listdir(music_dir) if file.endswith(('.mp3', '.wav'))]

            if songs:
                random_song = random.choice(songs)
                print("Playing:", random_song)

                pygame.mixer.init()

                pygame.mixer.music.load(os.path.join(music_dir, random_song))
                pygame.mixer.music.play()

                print("Press Enter to stop the music.")
                input()
                pygame.mixer.music.stop()
                print("Music stopped.")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H : %M : %S')
            speak(f"Sir, The time is {strTime}")
        elif 'quit' in query:
            speak("okay Goodbye!")
            exit()



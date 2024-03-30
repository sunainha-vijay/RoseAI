import os
import webbrowser
import datetime
import speech_recognition as sr
import pyttsx3
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import openai
import pygame
import re

# Initialize OpenAI API key
openai.api_key = '#'

# Initialize Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='e743c27af4964a32b064dc71dc5f5ceb',
                                               client_secret='254dca36402e4541a079140ff67c4067',
                                               redirect_uri='http://localhost:8888/callback',
                                               scope='user-library-read'))

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust the speaking rate

# Initialize Pygame for sound notification
pygame.init()
notification_sound = pygame.mixer.Sound("dance with mom dec-23.mp3")  # Replace with the path to your sound file

def play_notification_sound():
    pygame.mixer.Sound.play(notification_sound)
    pygame.time.wait(int(notification_sound.get_length() * 1000))  # Wait for the sound to finish

def speak(text):
    engine.say(text)
    engine.runAndWait()

def respond_to_greeting(activation_phrase):
    speak("Hello! How can I assist you today?")
    play_notification_sound()

def open_website(url):
    webbrowser.open(url)

def google_search(command):
    # Extract the search query from the command
    match = re.search(' search (.+?) ', command)
    if match:
        search_query = match.group(1)
        open_website(f'https://www.google.com/search?q={search_query}')
        speak(f"Searching {search_query} on Google.")
    else:
        speak("I'm sorry, I couldn't recognize the search query.")

def wikipedia_search(query):
    open_website(f'https://en.wikipedia.org/wiki/{query}')

def play_spotify_song(command):
    # Extract the song name from the command
    match = re.search(r'play (.+)', command)
    if match:
        song_name = match.group(1)
        if not song_name:
            speak("Please provide a valid song name.")
            return

        try:
            results = sp.search(q=song_name, type='track', limit=1)
            if results['tracks']['items']:
                track_uri = results['tracks']['items'][0]['uri']
                sp.start_playback(uris=[track_uri])
                speak(f"Now playing {song_name} on Spotify.")
            else:
                speak(f"Sorry, I couldn't find {song_name} on Spotify.")
        except spotipy.exceptions.SpotifyException as e:
            speak(f"Error: {e}")
    else:
        speak("I'm sorry, I couldn't recognize the song name.")

def play_spotify_music():
    try:
        sp.start_playback()
        speak("Now playing music on Spotify.")
    except spotipy.exceptions.SpotifyException as e:
        speak(f"Error: {e}")

def get_date_time():
    now = datetime.datetime.now()
    date = now.strftime("%d %B %Y")
    day = now.strftime("%A")
    time = now.strftime("%I:%M %p")
    speak(f"Today is {day}, {date}, and the time is {time}.")

def make_predictions():
    question = input("Ask me something: ")
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        temperature=0.7,
        max_tokens=150
    )
    answer = response['choices'][0]['text'].strip()
    speak(answer)

def main():
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Say 'Rose' to activate the assistant.")
            play_notification_sound()  # Play notification sound before listening
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            activation_phrase = recognizer.recognize_google(audio).lower()
            print(f"You said: {activation_phrase}")

            if 'rose' in activation_phrase:
                respond_to_greeting(activation_phrase)

                while True:  # Keep listening for commands until the user says 'exit'
                    speak("How can I assist you?")
                    with sr.Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source)
                        audio = recognizer.listen(source)

                    command = recognizer.recognize_google(audio).lower()
                    print(f"You said: {command}")

                    if 'search' in command:
                        google_search(command)

                    elif 'open youtube' in command:
                        open_website("https://www.youtube.com")

                    elif 'wikipedia ' in command:
                        wikipedia_search(command.replace('wikipedia search ', ''))

                    elif 'play' in command:
                        play_spotify_song(command)

                    elif 'play music' in command:
                        play_spotify_music()

                    elif 'time' in command:
                        get_date_time()

                    elif 'make predictions' in command:
                        make_predictions()

                    elif 'how are you' in command:
                        speak("I'm doing well, thank you!")

                    elif 'exit' in command:
                        speak("Goodbye!")
                        return

                    else:
                        speak("I'm sorry, I didn't understand that.")

        except sr.UnknownValueError:
            print("Sorry, I could not understand your request.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    main()

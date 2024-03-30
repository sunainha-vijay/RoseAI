# RoseAI Desktop Assistant

RoseAI is a Python-based desktop assistant that utilizes speech recognition and synthesis, along with integration with various APIs, to provide a range of functionalities, including playing music, fetching information from the internet, and assisting with daily tasks.

## Features

- Voice-activated interaction: Activate RoseAI by saying "Rose" and issue commands through speech.
- Music playback: Control Spotify to search for and play songs or start playing music directly.
- Web browsing: Perform Google searches, open YouTube, and access Wikipedia.
- Time and date: Retrieve current date, time, and day of the week.
- Prediction: Utilize OpenAI's GPT-3 model to make predictions or answer questions.
- Notification: Receive audible feedback through a notification sound.

## Installation

1. Clone the repository:

2. Install the required Python packages:

3. Set up Spotify API credentials:
- Create a Spotify Developer account and register your application.
- Obtain the client ID and client secret.
- Set the redirect URI to `http://localhost:8888/callback`.

4. Replace the placeholder API keys in the `main.py` file:
- Replace `'#'` with your OpenAI API key.
- Replace the `client_id` and `client_secret` with your Spotify API credentials.

5. Add a notification sound:
- Replace `"dance with mom dec-23.mp3"` with the path to your notification sound file.

6. Run the program:

## Usage

1. Activate RoseAI by saying "Rose" and wait for the response.
2. Issue commands using speech, such as:
- "Play the song <song_name>."
- "Search for <query>."
- "What's the time?"
- "Make predictions."
- "Exit."
3. Follow the assistant's responses or instructions.

## Credits

- This project utilizes the following libraries and APIs:
- SpeechRecognition
- pyttsx3
- spotipy (Spotify API)
- OpenAI API
- pygame

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

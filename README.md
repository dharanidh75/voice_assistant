FRIDAY Voice Assistant - Simple README
What is this?

A simple voice assistant that listens to you, uses AI to think, and talks back.
What you need:

    Python 3.8+

    A microphone

    Internet (for AI)

    Audio speakers

Quick Setup:
bash

# 1. Clone/download the project
git clone https://github.com/yourname/friday-assistant.git
cd friday-assistant

# 2. Install
pip install google-genai pyttsx3 SpeechRecognition python-dotenv

# 3. Create .env file
echo "GEMINI_API_KEY=your_key_here" > .env

# 4. Get API key from: https://aistudio.google.com/app/apikey

# 5. Run
python friday.py

How to use:

    Run the program

    Speak normally

    FRIDAY will respond

    Say "exit" to quit

Files:

    friday.py - Main program

    .env - Your API key (keep this secret!)

    requirements.txt - What to install

Problems?

    No sound? Check volume/microphone

    API errors? Get new key from Google AI Studio

    Installation issues? Use: pip install --upgrade pip

Made with:

    Python

    Google Gemini AI

    SpeechRecognition

    pyttsx3

Just run python friday.py and start talking! 🎤🤖

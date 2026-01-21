import os
import sys
from dotenv import load_dotenv
import google.genai as genai
import pyttsx3

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")
VOICE_SPEED = int(os.getenv("VOICE_SPEED", "160"))
VOICE_VOLUME = float(os.getenv("VOICE_VOLUME", "0.9"))

def validate_config():
    """Check if required environment variables are set"""
    errors = []
    
    if not GEMINI_API_KEY:
        errors.append("❌ GEMINI_API_KEY not found in .env file")
    elif GEMINI_API_KEY == "AIzaSyCLYmspOQFrKhUa0mVBr1v0K6FxMP8Ehlk":
        print("⚠️  Using default API key (may not work)")
    
    if not GEMINI_MODEL:
        errors.append("❌ GEMINI_MODEL not found in .env file")
    
    if errors:
        print("\n".join(errors))
        print("\n📋 Create a .env file with:")
        print("GEMINI_API_KEY=your_actual_key_here")
        print("GEMINI_MODEL=gemini-1.5-pro")
        return False
    
    return True

tts = pyttsx3.init()
tts.setProperty('rate', VOICE_SPEED)
tts.setProperty('volume', VOICE_VOLUME)

client = genai.Client(api_key=GEMINI_API_KEY)

def speak(text):
    """Speak text"""
    if not text:
        return
    
    text = text.replace('*', '').replace('_', '').replace('#', '')
    text = ' '.join(text.split())
    
    print(f"🤖 FRIDAY: {text}")
    tts.say(text)
    tts.runAndWait()

def get_user_input():
    """Get input from user"""
    print("\n🎤 Type your message (or 'exit' to quit):")
    user_input = input("You: ").strip()
    return user_input.lower() if user_input else None

def generate_response(text):
    """Generate AI response"""
    if not text:
        return "No input received.", False
    
    if text == "exit":
        return "Goodbye!", True
    
    if text == "clear":
        return "Chat cleared.", False
    
    if text == "config":
        config_info = f"""
        📋 Current Configuration:
        Model: {GEMINI_MODEL}
        Voice Speed: {VOICE_SPEED}
        Voice Volume: {VOICE_VOLUME}
        API Key: {GEMINI_API_KEY[:10]}...
        """
        return config_info.strip(), False
    
    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=text
        )
        return response.text, False
        
    except Exception as e:
        error_msg = str(e)
        
        if "404" in error_msg or "not found" in error_msg:
            try:
                response = client.models.generate_content(
                    model="gemini-1.0-pro",
                    contents=text
                )
                return response.text, False
            except:
                return f"Model {GEMINI_MODEL} not found. Check .env file.", False
        
        return f"Error: {error_msg[:80]}", False

def main():
    print("=" * 60)
    print("🤖 FRIDAY - Environment Configuration")
    print("=" * 60)
    
    if not validate_config():
        return
    
    print(f"✅ Using model: {GEMINI_MODEL}")
    print(f"✅ Voice speed: {VOICE_SPEED}")
    print(f"✅ Voice volume: {VOICE_VOLUME}")
    
    speak("Friday online. Configuration loaded from environment.")
    
    print("\n💬 Type to chat")
    print("⚙️  Type 'config' to see settings")
    print("🧠 Type 'clear' to reset")
    print("🚪 Type 'exit' to quit")
    print("-" * 50)
    
    while True:
        user_input = get_user_input()
        
        if not user_input:
            continue
        
        response, should_exit = generate_response(user_input)
        
        if should_exit:
            speak(response)
            break
        
        speak(response)
        print()

if __name__ == "__main__":
    main()
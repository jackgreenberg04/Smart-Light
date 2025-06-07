import speech_recognition as sr
import pyttsx3


def speak(text: str):
    """Use text-to-speech to speak a response."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def listen_for_command(timeout: int = 3, phrase_time_limit: int = 3):
    """Listen for voice command and return recognized text or None."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening for command...")
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            command = recognizer.recognize_google(audio).lower()
            print(f"Heard command: {command}")
            return command
        except sr.WaitTimeoutError:
            # No speech detected within timeout
            return None
        except sr.UnknownValueError:
            print("Could not understand audio. Please repeat.")
            speak("I didn't catch that. Please repeat your command.")
            return None
        except sr.RequestError as e:
            print(f"Speech recognition service error: {e}")
            return None


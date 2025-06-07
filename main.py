import time
from datetime import datetime

from clap_detection import detect_clap
from light_manager import LightManager
from logger import log_event
from voice_control import listen_for_command, speak


def main():
    manager = LightManager()
    print("Smart Light Guardian started. Say 'lights on', 'lights off', or 'light status'.")
    log_event("Session started")
    try:
        while True:
            command = listen_for_command(timeout=3, phrase_time_limit=3)
            if command:
                if "lights on" in command:
                    manager.turn_on("voice command")
                    speak("Lights turned on")
                elif "lights off" in command:
                    manager.turn_off("voice command")
                    speak("Lights turned off")
                elif "light status" in command:
                    status = "on" if manager.is_on else "off"
                    print(f"Light is currently {status}")
                    speak(f"Light is currently {status}")
                manager.last_interaction = datetime.now()
            else:
                if detect_clap():
                    manager.toggle("clap detection")
                    speak("Toggled light")
            manager.check_auto_off()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting Smart Light Guardian...")
    finally:
        summary = manager.summary()
        log_event("Session ended")
        print("Session Summary:")
        print(f"Times toggled: {summary['toggle_count']}")
        print(f"Total on time: {summary['total_on_time']}")
        print(f"Automatic shutoffs: {summary['auto_off_count']}")


if __name__ == "__main__":
    main()


# Smart Light Guardian

Smart Light Guardian is a simulated smart home light control system written in Python. It demonstrates voice and sound based accessibility features and energy-saving automation without requiring any physical hardware.

## Features

- **Voice Commands** – Say "lights on", "lights off", or "light status" to control the simulated light. Responses are also spoken back using text-to-speech.
- **Clap Detection** – A loud clap toggles the light for users who cannot speak commands.
- **Auto-Off Timer** – If no input is detected for five minutes, the light turns off automatically to conserve energy.
- **Logging** – All actions are recorded in `log.txt` with timestamps. A summary is printed when the program exits.

## Setup

1. Install Python 3.7+.
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure your computer has a working microphone.

## Usage

Run the main program:
```bash
python main.py
```
Say one of the supported commands or clap loudly to toggle the light. Press `Ctrl+C` to exit and see the session summary.

## Files

- `voice_control.py` – Handles speech recognition and text-to-speech.
- `clap_detection.py` – Detects loud sounds (claps).
- `light_manager.py` – Manages light state and inactivity timers.
- `logger.py` – Simple logging utility.
- `main.py` – Application entry point coordinating all modules.

This project is entirely simulated and meant for educational use.


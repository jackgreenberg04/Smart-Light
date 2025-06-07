import sounddevice as sd
import numpy as np


def detect_clap(duration: float = 0.5, threshold: float = 0.6, samplerate: int = 44100) -> bool:
    """Return True if a loud sound (clap) is detected."""
    try:
        recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
        sd.wait()
        amplitude = np.max(np.abs(recording))
        if amplitude > threshold:
            print("Clap detected")
            return True
    except Exception as e:
        print(f"Error detecting clap: {e}")
    return False


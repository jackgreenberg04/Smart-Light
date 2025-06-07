from datetime import datetime

LOG_FILE = "log.txt"


def log_event(message: str):
    """Append a timestamped event to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp}: {message}\n")


from datetime import datetime, timedelta
from logger import log_event


class LightManager:
    """Manage light state, timers, and energy usage."""

    def __init__(self, inactivity_minutes: int = 5):
        self.is_on = False
        self.inactivity = timedelta(minutes=inactivity_minutes)
        self.last_interaction = None
        self.last_on_time = None
        self.total_on_time = timedelta()
        self.toggle_count = 0
        self.auto_off_count = 0

    def _update_on_time(self):
        if self.is_on and self.last_on_time:
            self.total_on_time += datetime.now() - self.last_on_time
            self.last_on_time = datetime.now()

    def turn_on(self, source: str):
        if not self.is_on:
            self.is_on = True
            self.last_on_time = datetime.now()
            self.last_interaction = datetime.now()
            self.toggle_count += 1
            print(f"Lights turned ON via {source} at {self.last_on_time:%H:%M:%S}")
            log_event(f"Light turned ON via {source}")
        else:
            self.last_interaction = datetime.now()

    def turn_off(self, reason: str):
        if self.is_on:
            self._update_on_time()
            self.is_on = False
            print(f"Lights turned OFF ({reason}) at {datetime.now():%H:%M:%S}")
            log_event(f"Light turned OFF ({reason})")
            if reason == "inactivity":
                self.auto_off_count += 1
        self.last_interaction = datetime.now()

    def toggle(self, source: str):
        if self.is_on:
            self.turn_off(source)
        else:
            self.turn_on(source)

    def check_auto_off(self):
        if self.is_on and self.last_interaction:
            if datetime.now() - self.last_interaction > self.inactivity:
                self.turn_off("inactivity")

    def summary(self):
        if self.is_on:
            self._update_on_time()
            self.is_on = False
        return {
            "toggle_count": self.toggle_count,
            "total_on_time": self.total_on_time,
            "auto_off_count": self.auto_off_count,
        }


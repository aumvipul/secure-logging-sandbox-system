import hashlib
import time
import json
from config import LOG_FILE

class LogEntry:
    def __init__(self, index, timestamp, event, description, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.event = event
        self.description = description
        self.prev_hash = prev_hash
        self.current_hash = self.generate_hash()

    def generate_hash(self):
        data = f"{self.index}{self.timestamp}{self.event}{self.description}{self.prev_hash}"
        return hashlib.sha256(data.encode()).hexdigest()

    def to_dict(self):
        return self.__dict__


class TamperEvidentLogger:
    def __init__(self):
        self.logs = []
        self.load_logs()

    def load_logs(self):
        try:
            with open(LOG_FILE, "r") as f:
                self.logs = json.load(f)
        except:
            self.logs = []

    def save_logs(self):
        with open(LOG_FILE, "w") as f:
            json.dump(self.logs, f, indent=4)

    def add_log(self, event, description):
        index = len(self.logs)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        prev_hash = self.logs[-1]["current_hash"] if self.logs else "0"

        new_entry = LogEntry(index, timestamp, event, description, prev_hash)
        self.logs.append(new_entry.to_dict())

        self.save_logs()
        return new_entry

    def get_logs(self):
        return self.logs
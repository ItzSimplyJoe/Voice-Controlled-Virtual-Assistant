import datetime
import time
import re

from Speech.voiceinput import voiceinput
from Speech.voiceoutput import voiceoutput
    
class Reminder:
    def create_reminder(self, text):
        tokens = text.split()

        keywords = {
            "set": "reminder",
            "reminder": "for",
            "to": "task",
            "at": "time",
        }
        dictionary = {}
        for token in tokens:
            if token in keywords:
                dictionary[keywords[token]] = tokens[tokens.index(token) + 1]
        if not re.match(r"\d{1,2}:\d{1,2}", dictionary["time"]):
            voiceoutput.speak("At what time do you want to set the reminder?")
            time = voiceinput.audio_to_text()
        if "task" not in dictionary:
            dictionary["task"] = "reminder"
        self.time = dictionary["time"]
        self.message = dictionary["task"]
        voiceoutput.speak("Reminder set for " + self.time + " for " + self.message)

    def main(self):
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")
            if current_time == self.time:
                voiceoutput.speak(self.message)
            else:
                pass

reminder = Reminder()
if __name__ == "__main__":
    reminder.create_reminder("set reminder to call mom at 10:30")

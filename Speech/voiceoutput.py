import pyttsx3
class VoiceOutput:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
    
    def stop(self):
        self.engine.stop()
    
voiceoutput = VoiceOutput()

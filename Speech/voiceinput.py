import pvporcupine
import pyaudio
import struct
import speech_recognition as sr
import threading
from Speech.voiceoutput import voiceoutput

from Functions.Timer.timer import timer
from Functions.Music.player import musicplayer

class VoiceInput:
    def __init__(self):
        self.porcupine = None
        self.pa = None
        self.audio_stream = None
        self.voice_thread = None

    def initialize_voice(self):
        self.porcupine = pvporcupine.create(
            access_key="k+dAStF62RACtJcNtYFHyseWvW7mWw6fFuUrpPDDeXZ0UA44VVIBZA==",
            keyword_paths=['Speech/minijoe.ppn'],
            keywords=['Mini Joe']
        )
        self.pa = pyaudio.PyAudio()
        self.audio_stream = self.pa.open(
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_length
        )
        print("Voice initialized")

    def process_voice_input(self):
        while True:
            pcm = self.audio_stream.read(self.porcupine.frame_length)
            pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)
            keyword_index = self.porcupine.process(pcm)
            if keyword_index >= 0:
                threading.Thread(target=voiceoutput.stop, args=()).start()
                threading.Thread(target=timer.timer_stop, args=()).start()
                threading.Thread(target=musicplayer.stop, args=()).start()
                text = self.audio_to_text()
                return(text)

    def audio_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.non_speaking_duration = 0.5
            audio = recognizer.listen(source,timeout=7, phrase_time_limit=5)
        try:
            text = recognizer.recognize_google(audio)
            print("Voice input:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't understand.")
            threading.Thread(target=voiceoutput.speak, args=("Sorry, I didn't understand.")).start()
        except sr.RequestError as e:
            print("There was an error processing the voice input:", str(e))
            threading.Thread(target=voiceoutput.speak, args=("There was an error processing the voice input.")).start()


voiceinput = VoiceInput()
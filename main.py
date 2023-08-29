from ML.Intent_Classification import intent_classifier
from ML.NLP import nlp

from Speech.voiceinput import voiceinput
from Speech.voiceoutput import voiceoutput

from Functions.webanswers.webanswers import webanswers
from Functions.Music.player import musicplayer
from Functions.Timer.timer import timer
from Functions.Location.location import location
from Functions.Conversations.conversation import conversation
from Functions.Location.weather import weather
from Functions.Conversions.conversion import conversions
from Functions.Maths.maths import maths

import threading


class Assistant:
    def __init__(self, name):
        self.name = name

    def reply(self, text):
        text = nlp.predict(text)
        intent = intent_classifier.predict(text)

        replies = {
            'webanswer': webanswers.get_answer,
            'timer': timer.main,
            'music': musicplayer.main,
            'location': location.main,
            'greetings': conversation.reply,
            'leavings' : conversation.reply,
            'jokes' : conversation.reply,
            'insults' : conversation.reply,
            'compliments' : conversation.reply,
            'personality' : conversation.reply,
            'weather': weather.main,
            'conversions': conversions.main,
        }

        try:
            reply_func = replies[intent]
            if callable(reply_func):
                response = reply_func(text)
                return response
        except KeyError:
            print("Sorry, I didn't understand.")
            pass
        except Exception as e:
            print("There has been an error. Please report this to Joe :D")
            print("Error:", str(e))
        
    def main(self):
        while True:
            voiceinput.initialize_voice()
            text = voiceinput.process_voice_input()
            print(text)
            if text:
                output = threading.Thread(target=self.reply, args=(text,)).start()
                if output:
                    print(output)
                    threading.Thread(target=voiceoutput.speak, args=(output,)).start()
            else:
                pass
assistant = Assistant("Badger")
assistant.main()
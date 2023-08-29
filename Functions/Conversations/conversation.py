import json
from ML.detemine_most_similar import determine_most_similar_phrase
import random
class Conversation:
    def reply(self,text,intent):
        with open(f'Functions/Conversations/{intent}.json') as samplesfile:  
            samples = json.load(samplesfile)

        most_similar = determine_most_similar_phrase(text = text, intent_dict = samples)

        if type(samples[most_similar]) == str:
            print(samples[most_similar])
            return(samples[most_similar])
        elif type(samples[most_similar]) == list:
            new = random.choice(samples[most_similar])
            print(new)
            return(new)
        else:
            print("Sorry, I didn't understand.")
            return("Sorry, I didn't understand.")

conversation = Conversation()
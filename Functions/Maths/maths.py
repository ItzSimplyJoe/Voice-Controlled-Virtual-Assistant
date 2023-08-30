from ML.detemine_most_similar import determine_most_similar_phrase
from Functions.Maths.solvers import *

class Maths:
    def main(self,text):
        samples = {
            "what is 18 + 64" : {'function' : general_calculations},
            "what is 18 - 64" : {'function' : general_calculations},
            "what is 18 * 64" : {'function' : general_calculations},
            "what is 18 / 64" : {'function' : general_calculations},
            "what is 18 + 64 + 64" : {'function' : general_calculations},
            "what is 18 - 64 - 64" : {'function' : general_calculations},
            "what is 18 * 64 * 64" : {'function' : general_calculations},
            "what is 18 / 64 / 64" : {'function' : general_calculations},
            "what is 18 + 64 + 64 + 64" : {'function' : general_calculations},
            "what is 18 - 64 - 64 - 64" : {'function' : general_calculations},
            "what is sin 90" : {'function' : find_sin},
            "what is cos 90" : {'function' : find_cos},
            "what is tan 90" : {'function' : find_tan},
            "what is sin 90 + 90" : {'function' : find_sin},
            "what is cos 90 + 90" : {'function' : find_cos},
            "what is tan 90 + 90" : {'function' : find_tan},
        }

        most_similar = determine_most_similar_phrase(text, samples)
        function = samples[most_similar]['function']
        text = self.modify_sentence(text)
        print(text)
        return (function(text))
    
    def modify_sentence(self, text):
        valid_chars = "0123456789+-*/x^"
        modified_text = ''.join(char for char in text if char in valid_chars)
        return modified_text
     
maths = Maths()

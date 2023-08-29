from ML.detemine_most_similar import determine_most_similar_phrase
import geocoder
class Location:

    def main(self, text):
        samples = {
            "where are we" : {'function' : self.say_location, 'type' : 'location'},
            "location" : {'function' : self.say_location, 'type' : 'location'},
            "city" : {'function' : self.say_location, 'type' : 'city'},
            "state" : {'function' : self.say_location, 'type' : 'state'},
            "country" : {'function' : self.say_location, 'type' : 'country'}
        }

        most_similar = determine_most_similar_phrase(text, samples)
        function = samples[most_similar]['function']
        function(samples[most_similar]['type'])

    def get_lat_lng(self):
        g = geocoder.ip('me')
        return g.latlng[0], g.latlng[1]

    def get_city_state_country(self):
        g = geocoder.ip('me')

        return [g.city, g.state, g.country]

    def say_location(self, type):
        if type == 'location':
            print(" ".join(self.get_city_state_country()))
            return(" ".join(self.get_city_state_country()))
        if type == 'city':
            print(self.get_city_state_country()[0])
            return(self.get_city_state_country()[0])
        if type == 'state':
            print(self.get_city_state_country()[0])
            return(self.get_city_state_country()[1])
        if type == 'country':
            print(self.get_city_state_country()[0])
            return(self.get_city_state_country()[2])

location = Location()
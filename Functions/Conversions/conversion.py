from ML.detemine_most_similar import determine_most_similar_phrase

class Conversions:
    def convert_units(self, value, from_unit, to_unit):
        conversion_factor = {
            "celsius": {"fahrenheit": lambda x: (x * 9/5) + 32, "kelvin": lambda x: x + 273.15},
            "fahrenheit": {"celsius": lambda x: (x - 32) * 5/9, "kelvin": lambda x: (x + 459.67) * 5/9},
            "kelvin": {"celsius": lambda x: x - 273.15, "fahrenheit": lambda x: (x * 9/5) - 459.67},
            "inches" : {"centimeters": lambda x: x * 2.54, "meters": lambda x: x * 0.0254, "feet": lambda x: x * 0.0833333, "yards": lambda x: x * 0.0277778, "miles": lambda x: x * 0.0000157828},
            "centimeters" : {"inches": lambda x: x * 0.393701, "meters": lambda x: x * 0.01, "feet": lambda x: x * 0.0328084, "yards": lambda x: x * 0.0109361, "miles": lambda x: x * 0.0000062137},
            "meters" : {"inches": lambda x: x * 39.3701, "centimeters": lambda x: x * 100, "feet": lambda x: x * 3.28084, "yards": lambda x: x * 1.09361, "miles": lambda x: x * 0.000621371},
            "feet" : {"inches": lambda x: x * 12, "centimeters": lambda x: x * 30.48, "meters": lambda x: x * 0.3048, "yards": lambda x: x * 0.333333, "miles": lambda x: x * 0.000189394},
            "yards" : {"inches": lambda x: x * 36, "centimeters": lambda x: x * 91.44, "meters": lambda x: x * 0.9144, "feet": lambda x: x * 3, "miles": lambda x: x * 0.000568182},
            "miles" : {"inches": lambda x: x * 63360, "centimeters": lambda x: x * 160934, "meters": lambda x: x * 1609.34, "feet": lambda x: x * 5280, "yards": lambda x: x * 1760},
            "grams" : {"kilograms": lambda x: x * 0.001, "pounds": lambda x: x * 0.00220462, "ounces": lambda x: x * 0.035274},
            "kilograms" : {"grams": lambda x: x * 1000, "pounds": lambda x: x * 2.20462, "ounces": lambda x: x * 35.274},
            "pounds" : {"grams": lambda x: x * 453.592, "kilograms": lambda x: x * 0.453592, "ounces": lambda x: x * 16},
            "ounces" : {"grams": lambda x: x * 28.3495, "kilograms": lambda x: x * 0.0283495, "pounds": lambda x: x * 0.0625},
            "seconds" : {"minutes": lambda x: x * 0.0166667, "hours": lambda x: x * 0.000277778, "days": lambda x: x * 0.0000115741, "weeks": lambda x: x * 0.0000016534, "years": lambda x: x * 0.0000000316881},
            "minutes" : {"seconds": lambda x: x * 60, "hours": lambda x: x * 0.0166667, "days": lambda x: x * 0.000694444, "weeks": lambda x: x * 0.0000992063, "years": lambda x: x * 0.0000019026},
            "hours" : {"seconds": lambda x: x * 3600, "minutes": lambda x: x * 60, "days": lambda x: x * 0.0416667, "weeks": lambda x: x * 0.00595238, "years": lambda x: x * 0.000114155},
            "days" : {"seconds": lambda x: x * 86400, "minutes": lambda x: x * 1440, "hours": lambda x: x * 24, "weeks": lambda x: x * 0.142857, "years": lambda x: x * 0.00273973},
            "weeks" : {"seconds": lambda x: x * 604800, "minutes": lambda x: x * 10080, "hours": lambda x: x * 168, "days": lambda x: x * 7, "years": lambda x: x * 0.0191781},
            "years" : {"seconds": lambda x: x * 31536000, "minutes": lambda x: x * 525600, "hours": lambda x: x * 8760, "days": lambda x: x * 365, "weeks": lambda x: x * 52.1429},
            "millimeters" : {"centimeters": lambda x: x * 0.1, "meters": lambda x: x * 0.001, "kilometers": lambda x: x * 0.000001, "inches": lambda x: x * 0.0393701, "feet": lambda x: x * 0.00328084, "yards": lambda x: x * 0.00109361, "miles": lambda x: x * 0.000000621371},
        }
        result = conversion_factor[from_unit][to_unit](value)
        return f"{value} {from_unit} is equal to {result:.2f} {to_unit}."
    
    def main(self,text):
        samples = {
            'convert 30cm to inches' : {'function' : self.convert_units, 'from_unit': 'centimeters', 'to_unit': 'inches'},
            'convert 30 centimeters to inches' : {'function' : self.convert_units, 'from_unit': 'centimeters', 'to_unit': 'inches'},
            'convert 30 degrees celcius to fahrenheit' : {'function' : self.convert_units, 'from_unit': 'celsius', 'to_unit': 'fahrenheit'},
            'convert 30 degrees celcius to kelvin' : {'function' : self.convert_units, 'from_unit': 'celsius', 'to_unit': 'kelvin'},
            'convert 30 degrees fahrenheit to celcius' : {'function' : self.convert_units, 'from_unit': 'fahrenheit', 'to_unit': 'celsius'},
            'convert 30 degrees fahrenheit to kelvin' : {'function' : self.convert_units, 'from_unit': 'fahrenheit', 'to_unit': 'kelvin'},
            'convert 30 kelvin to celcius' : {'function' : self.convert_units, 'from_unit': 'kelvin', 'to_unit': 'celsius'},
            'convert 30 kelvin to fahrenheit' : {'function' : self.convert_units, 'from_unit': 'kelvin', 'to_unit': 'fahrenheit'},
            'convert 30 inches to centimeters' : {'function' : self.convert_units, 'from_unit': 'inches', 'to_unit': 'centimeters'},
            'convert 30 inches to meters' : {'function' : self.convert_units, 'from_unit': 'inches', 'to_unit': 'meters'},
            'convert 30 inches to feet' : {'function' : self.convert_units, 'from_unit': 'inches', 'to_unit': 'feet'},
            'convert 30 inches to yards' : {'function' : self.convert_units, 'from_unit': 'inches', 'to_unit': 'yards'},
            'convert 30 inches to miles' : {'function' : self.convert_units, 'from_unit': 'inches', 'to_unit': 'miles'},
            'convert 30 centimeters to inches' : {'function' : self.convert_units, 'from_unit': 'centimeters', 'to_unit': 'inches'},
            'convert 30 centimeters to meters' : {'function' : self.convert_units, 'from_unit': 'centimeters', 'to_unit': 'meters'},
            'convert 30 centimeters to feet' : {'function' : self.convert_units, 'from_unit': 'centimeters', 'to_unit': 'feet'},
            'convert 30 centimeters to yards' : {'function' : self.convert_units, 'from_unit': 'centimeters', 'to_unit': 'yards'},
            'convert 30 centimeters to miles' : {'function' : self.convert_units, 'from_unit': 'centimeters', 'to_unit': 'miles'},
            'convert 30 meters to inches' : {'function' : self.convert_units, 'from_unit': 'meters', 'to_unit': 'inches'},
            'convert 30 meters to centimeters' : {'function' : self.convert_units, 'from_unit': 'meters', 'to_unit': 'centimeters'},
            'convert 30 meters to feet' : {'function' : self.convert_units, 'from_unit': 'meters', 'to_unit': 'feet'},
            'convert 30 meters to yards' : {'function' : self.convert_units, 'from_unit': 'meters', 'to_unit': 'yards'},
            'convert 30 meters to miles' : {'function' : self.convert_units, 'from_unit': 'meters', 'to_unit': 'miles'},
            'convert 30 feet to inches' : {'function' : self.convert_units, 'from_unit': 'feet', 'to_unit': 'inches'},
            'convert 30 feet to centimeters' : {'function' : self.convert_units, 'from_unit': 'feet', 'to_unit': 'centimeters'},
            'convert 30 feet to meters' : {'function' : self.convert_units, 'from_unit': 'feet', 'to_unit': 'meters'},
            'convert 30 feet to yards' : {'function' : self.convert_units, 'from_unit': 'feet', 'to_unit': 'yards'},
            'convert 30 feet to miles' : {'function' : self.convert_units, 'from_unit': 'feet', 'to_unit': 'miles'},
            'convert 30 yards to inches' : {'function' : self.convert_units, 'from_unit': 'yards', 'to_unit': 'inches'},
            'convert 30 yards to centimeters' : {'function' : self.convert_units, 'from_unit': 'yards', 'to_unit': 'centimeters'},
            'convert 30 yards to meters' : {'function' : self.convert_units, 'from_unit': 'yards', 'to_unit': 'meters'},
            'convert 30 yards to feet' : {'function' : self.convert_units, 'from_unit': 'yards', 'to_unit': 'feet'},
            'convert 30 yards to miles' : {'function' : self.convert_units, 'from_unit': 'yards', 'to_unit': 'miles'},
            'convert 30 miles to inches' : {'function' : self.convert_units, 'from_unit': 'miles', 'to_unit': 'inches'},
            'convert 30 miles to centimeters' : {'function' : self.convert_units, 'from_unit': 'miles', 'to_unit': 'centimeters'},
            'convert 30 miles to meters' : {'function' : self.convert_units, 'from_unit': 'miles', 'to_unit': 'meters'},
            'convert 30 miles to feet' : {'function' : self.convert_units, 'from_unit': 'miles', 'to_unit': 'feet'},
            'convert 30 miles to yards' : {'function' : self.convert_units, 'from_unit': 'miles', 'to_unit': 'yards'},
            'convert 30 grams to kilograms' : {'function' : self.convert_units, 'from_unit': 'grams', 'to_unit': 'kilograms'},
            'convert 30 grams to pounds' : {'function' : self.convert_units, 'from_unit': 'grams', 'to_unit': 'pounds'},
            'convert 30 grams to ounces' : {'function' : self.convert_units, 'from_unit': 'grams', 'to_unit': 'ounces'},
            'convert 30 kilograms to grams' : {'function' : self.convert_units, 'from_unit': 'kilograms', 'to_unit': 'grams'},
            'convert 30 kilograms to pounds' : {'function' : self.convert_units, 'from_unit': 'kilograms', 'to_unit': 'pounds'},
            'convert 30 kilograms to ounces' : {'function' : self.convert_units, 'from_unit': 'kilograms', 'to_unit': 'ounces'},
            'convert 30 pounds to grams' : {'function' : self.convert_units, 'from_unit': 'pounds', 'to_unit': 'grams'},
            'convert 30 pounds to kilograms' : {'function' : self.convert_units, 'from_unit': 'pounds', 'to_unit': 'kilograms'},
            'convert 30 pounds to ounces' : {'function' : self.convert_units, 'from_unit': 'pounds', 'to_unit': 'ounces'},
            'convert 30 ounces to grams' : {'function' : self.convert_units, 'from_unit': 'ounces', 'to_unit': 'grams'},
            'convert 30 ounces to kilograms' : {'function' : self.convert_units, 'from_unit': 'ounces', 'to_unit': 'kilograms'},
            'convert 30 ounces to pounds' : {'function' : self.convert_units, 'from_unit': 'ounces', 'to_unit': 'pounds'},
            'convert 30 seconds to minutes' : {'function' : self.convert_units, 'from_unit': 'seconds', 'to_unit': 'minutes'},
            'convert 30 seconds to hours' : {'function' : self.convert_units, 'from_unit': 'seconds', 'to_unit': 'hours'},
            'convert 30 seconds to days' : {'function' : self.convert_units, 'from_unit': 'seconds', 'to_unit': 'days'},
            'convert 30 seconds to weeks' : {'function' : self.convert_units, 'from_unit': 'seconds', 'to_unit': 'weeks'},
            'convert 30 seconds to years' : {'function' : self.convert_units, 'from_unit': 'seconds', 'to_unit': 'years'},
            'convert 30 minutes to seconds' : {'function' : self.convert_units, 'from_unit': 'minutes', 'to_unit': 'seconds'},
            'convert 30 minutes to hours' : {'function' : self.convert_units, 'from_unit': 'minutes', 'to_unit': 'hours'},
            'convert 30 minutes to days' : {'function' : self.convert_units, 'from_unit': 'minutes', 'to_unit': 'days'},
            'convert 30 minutes to weeks' : {'function' : self.convert_units, 'from_unit': 'minutes', 'to_unit': 'weeks'},
            'convert 30 minutes to years' : {'function' : self.convert_units, 'from_unit': 'minutes', 'to_unit': 'years'},
            'convert 30 hours to seconds' : {'function' : self.convert_units, 'from_unit': 'hours', 'to_unit': 'seconds'},
            'convert 30 hours to minutes' : {'function' : self.convert_units, 'from_unit': 'hours', 'to_unit': 'minutes'},
            'convert 30 hours to days' : {'function' : self.convert_units, 'from_unit': 'hours', 'to_unit': 'days'},
            'convert 30 hours to weeks' : {'function' : self.convert_units, 'from_unit': 'hours', 'to_unit': 'weeks'},
            'convert 30 hours to years' : {'function' : self.convert_units, 'from_unit': 'hours', 'to_unit': 'years'},
            'convert 30 days to seconds' : {'function' : self.convert_units, 'from_unit': 'days', 'to_unit': 'seconds'},
            'convert 30 days to minutes' : {'function' : self.convert_units, 'from_unit': 'days', 'to_unit': 'minutes'},
            'convert 30 days to hours' : {'function' : self.convert_units, 'from_unit': 'days', 'to_unit': 'hours'},
            'convert 30 days to weeks' : {'function' : self.convert_units, 'from_unit': 'days', 'to_unit': 'weeks'},
            'convert 30 days to years' : {'function' : self.convert_units, 'from_unit': 'days', 'to_unit': 'years'},
            'convert 30 weeks to seconds' : {'function' : self.convert_units, 'from_unit': 'weeks', 'to_unit': 'seconds'},
            'convert 30 weeks to minutes' : {'function' : self.convert_units, 'from_unit': 'weeks', 'to_unit': 'minutes'},
            'convert 30 weeks to hours' : {'function' : self.convert_units, 'from_unit': 'weeks', 'to_unit': 'hours'},
            'convert 30 weeks to days' : {'function' : self.convert_units, 'from_unit': 'weeks', 'to_unit': 'days'},
            'convert 30 weeks to years' : {'function' : self.convert_units, 'from_unit': 'weeks', 'to_unit': 'years'},
            'convert 30 years to seconds' : {'function' : self.convert_units, 'from_unit': 'years', 'to_unit': 'seconds'},
            'convert 30 years to minutes' : {'function' : self.convert_units, 'from_unit': 'years', 'to_unit': 'minutes'},
            'convert 30 years to hours' : {'function' : self.convert_units, 'from_unit': 'years', 'to_unit': 'hours'},
            'convert 30 years to days' : {'function' : self.convert_units, 'from_unit': 'years', 'to_unit': 'days'},
            'convert 30 years to weeks' : {'function' : self.convert_units, 'from_unit': 'years', 'to_unit': 'weeks'},
            'convert 30 millimeters to centimeters' : {'function' : self.convert_units, 'from_unit': 'millimeters', 'to_unit': 'centimeters'},
            'convert 30 millimeters to meters' : {'function' : self.convert_units, 'from_unit': 'millimeters', 'to_unit': 'meters'},
            'convert 30 millimeters to kilometers' : {'function' : self.convert_units, 'from_unit': 'millimeters', 'to_unit': 'kilometers'},
            'convert 30 millimeters to inches' : {'function' : self.convert_units, 'from_unit': 'millimeters', 'to_unit': 'inches'},
            'convert 30 millimeters to feet' : {'function' : self.convert_units, 'from_unit': 'millimeters', 'to_unit': 'feet'},
            'convert 30 millimeters to yards' : {'function' : self.convert_units, 'from_unit': 'millimeters', 'to_unit': 'yards'},
            'convert 30 millimeters to miles' : {'function' : self.convert_units, 'from_unit': 'millimeters', 'to_unit': 'miles'}
        }
        most_similar = determine_most_similar_phrase(text, samples)
        func = samples[most_similar]['function']
        from_unit = samples[most_similar]['from_unit']
        to_unit = samples[most_similar]['to_unit']
        tempvar = func(30, from_unit, to_unit)
        return tempvar
    
conversions = Conversions()
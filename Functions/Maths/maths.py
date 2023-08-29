from ML.detemine_most_similar import determine_most_similar_phrase
import math
import sympy

class Maths:
    def main(self,text):
        samples = {
            "what is 18 + 64" : {'function' : self.general_calculations},
            "what is 18 - 64" : {'function' : self.general_calculations},
            "what is 18 * 64" : {'function' : self.general_calculations},
            "what is 18 / 64" : {'function' : self.general_calculations},
            "what is 18 + 64 + 64" : {'function' : self.general_calculations},
            "what is 18 - 64 - 64" : {'function' : self.general_calculations},
            "what is 18 * 64 * 64" : {'function' : self.general_calculations},
            "what is 18 / 64 / 64" : {'function' : self.general_calculations},
            "what is 18 + 64 + 64 + 64" : {'function' : self.general_calculations},
            "what is 18 - 64 - 64 - 64" : {'function' : self.general_calculations},
            "what is the derivative of x^2" : {'function' : self.find_derivative},
            "what is the derivative of x^3" : {'function' : self.find_derivative},
            "solve x^2 + 2x + 1" : {'function' : self.solve_equation},
            "solve x^3 + 2x^2 + 1" : {'function' : self.solve_equation},
            "integrate x^2 + 2x + 1" : {'function' : self.find_integral},
            "integrate x^3 + 2x^2 + 1" : {'function' : self.find_integral},
            "limit x^2 + 2x + 1" : {'function' : self.find_limit},
            "limit x^3 + 2x^2 + 1" : {'function' : self.find_limit},
            "sum x^2 + 2x + 1" : {'function' : self.find_sum},
            "sum x^3 + 2x^2 + 1" : {'function' : self.find_sum},
            "product x^2 + 2x + 1" : {'function' : self.find_product},
            "product x^3 + 2x^2 + 1" : {'function' : self.find_product},
            "factorial 5" : {'function' : self.find_factorial},
            "factorial 10" : {'function' : self.find_factorial},
            "gcd 5 10" : {'function' : self.find_gcd},
            "gcd 10 20" : {'function' : self.find_gcd},
            "lcm 5 10" : {'function' : self.find_lcm},
            "lcm 10 20" : {'function' : self.find_lcm},
            "sqrt 5" : {'function' : self.find_sqrt},
            "sqrt 10" : {'function' : self.find_sqrt},
            "log 5" : {'function' : self.find_log},
            "log 10" : {'function' : self.find_log},
            "sin 5" : {'function' : self.find_sin},
            "sin 10" : {'function' : self.find_sin},
            "cos 5" : {'function' : self.find_cos},
            "cos 10" : {'function' : self.find_cos},
            "tan 5" : {'function' : self.find_tan},
            "tan 10" : {'function' : self.find_tan},
            "cot 5" : {'function' : self.find_cot},
            "cot 10" : {'function' : self.find_cot},
            "sec 5" : {'function' : self.find_sec},
            "sec 10" : {'function' : self.find_sec},
            "cosec 5" : {'function' : self.find_cosec},
            "cosec 10" : {'function' : self.find_cosec},
            "asin 5" : {'function' : self.find_asin},
            "asin 10" : {'function' : self.find_asin},
            "acos 5" : {'function' : self.find_acos},
            "acos 10" : {'function' : self.find_acos},
            "atan 5" : {'function' : self.find_atan},
            "atan 10" : {'function' : self.find_atan},
            "acot 5" : {'function' : self.find_acot},
            "acot 10" : {'function' : self.find_acot},
            "asec 5" : {'function' : self.find_asec},
            "asec 10" : {'function' : self.find_asec},
            "acosec 5" : {'function' : self.find_acosec},
            "acosec 10" : {'function' : self.find_acosec},
            "sinh 5" : {'function' : self.find_sinh},
            "sinh 10" : {'function' : self.find_sinh},
            "cosh 5" : {'function' : self.find_cosh},
            "cosh 10" : {'function' : self.find_cosh},
            "tanh 5" : {'function' : self.find_tanh},
            "tanh 10" : {'function' : self.find_tanh},
            "coth 5" : {'function' : self.find_coth},
            "coth 10" : {'function' : self.find_coth},
            "sech 5" : {'function' : self.find_sech},
            "sech 10" : {'function' : self.find_sech},
            "cosech 5" : {'function' : self.find_cosech},
            "cosech 10" : {'function' : self.find_cosech},
        }

        most_similar = determine_most_similar_phrase(text, samples)
        function = samples[most_similar]['function']
        return (function(text))

    def general_calculations(self, text):
        valid_chars = "0123456789+-*/"
        modified_text = ''.join(char for char in text if char in valid_chars)
        try:
            result = eval(modified_text)
            return f"The answer is {result}"
        except Exception as e:
            return f"Error: {e}"
        
    def solve_equation(self, text):
        try:
            equation = text.split("solve ")[-1]
            x = sympy.symbols('x')
            result = sympy.solve(equation, x)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_derivative(self, text):
        try:
            equation = text.split("differentiate ")[-1]
            x = sympy.symbols('x')
            result = sympy.diff(equation, x)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_integral(self, text):
        try:
            equation = text.split("integrate ")[-1]
            x = sympy.symbols('x')
            result = sympy.integrate(equation, x)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_limit(self, text):
        try:
            equation = text.split("limit ")[-1]
            x = sympy.symbols('x')
            result = sympy.limit(equation, x, 0)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_sum(self, text):
        try:
            equation = text.split("sum ")[-1]
            x = sympy.symbols('x')
            result = sympy.summation(equation, (x, 0, 10))
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_product(self, text):
        try:
            equation = text.split("product ")[-1]
            x = sympy.symbols('x')
            result = sympy.product(equation, (x, 0, 10))
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_factorial(self, text):
        try:
            equation = text.split("factorial ")[-1]
            result = math.factorial(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_gcd(self, text):
        try:
            equation = text.split("gcd ")[-1]
            result = math.gcd(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_lcm(self, text):
        try:
            equation = text.split("lcm ")[-1]
            result = math.lcm(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_sqrt(self, text):
        try:
            equation = text.split("sqrt ")[-1]
            result = math.sqrt(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_log(self, text):
        try:
            equation = text.split("log ")[-1]
            result = math.log(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_sin(self, text):
        try:
            equation = text.split("sin ")[-1]
            result = math.sin(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_cos(self, text):
        try:
            equation = text.split("cos ")[-1]
            result = math.cos(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_tan(self, text):
        try:
            equation = text.split("tan ")[-1]
            result = math.tan(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_cot(self, text):
        try:
            equation = text.split("cot ")[-1]
            result = math.cot(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_sec(self, text):
        try:
            equation = text.split("sec ")[-1]
            result = math.sec(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_cosec(self, text):
        try:
            equation = text.split("cosec ")[-1]
            result = math.cosec(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_asin(self, text):
        try:
            equation = text.split("asin ")[-1]
            result = math.asin(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_acos(self, text):
        try:
            equation = text.split("acos ")[-1]
            result = math.acos(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_atan(self, text):
        try:
            equation = text.split("atan ")[-1]
            result = math.atan(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_acot(self, text):
        try:
            equation = text.split("acot ")[-1]
            result = math.acot(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_asec(self, text):
        try:
            equation = text.split("asec ")[-1]
            result = math.asec(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_acosec(self, text):
        try:
            equation = text.split("acosec ")[-1]
            result = math.acosec(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_sinh(self, text):
        try:
            equation = text.split("sinh ")[-1]
            result = math.sinh(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_cosh(self, text):
        try:
            equation = text.split("cosh ")[-1]
            result = math.cosh(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_tanh(self, text):
        try:
            equation = text.split("tanh ")[-1]
            result = math.tanh(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_coth(self, text):
        try:
            equation = text.split("coth ")[-1]
            result = math.coth(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_sech(self, text):
        try:
            equation = text.split("sech ")[-1]
            result = math.sech(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."
        
    def find_cosech(self, text):
        try:
            equation = text.split("cosech ")[-1]
            result = math.cosech(equation)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't solve the problem."     
           
maths = Maths()
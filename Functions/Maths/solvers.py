import math
import sympy

def general_calculations(text):
        try:
            result = eval(text)
            return f"The answer is {result}"
        except Exception as e:
            return f"Error: {e}"

def find_sin(text):
    try:
        result = math.sin(eval(text))
        return f"The answer is {result}"
    except Exception as e:
        return f"Error: {e}"
    
def find_cos(text):
    try:
        result = math.cos(eval(text))
        return f"The answer is {result}"
    except Exception as e:
        return f"Error: {e}"
    
def find_tan(text):
    try:
        result = math.tan(eval(text))
        return f"The answer is {result}"
    except Exception as e:
        return f"Error: {e}"
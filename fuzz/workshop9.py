'''
Author: Akond Rahman 
Code needed for Workshop 9
'''

import random 
import json

def divide(v1, v2):
   return v1 / v2 

def add(v1, v2):
   return v1 + v2 

def sub(v1, v2):
   return v1 - v2 

def mult(v1, v2):
   return v1 * v2 

def remaind(v1, v2):
   return v1 % v2 

def pow(v1, v2):
   return v1 ^ v2 

def fuzzValuesDiv(val1, val2):
   res = divide(val1, val2)
   return res  

def fuzzValuesAdd(val1, val2):
   res = add(val1, val2)
   return res  

def fuzzValuesSub(val1, val2):
   res = sub(val1, val2)
   return res  

def fuzzValuesMult(val1, val2):
   res = mult(val1, val2)
   return res  

def fuzzValuesRemaind(val1, val2):
   res = remaind(val1, val2)
   return res  

def fuzzValuesPow(val1, val2):
   res = pow(val1, val2)
   return res  

def simpleFuzzer(func): 
    # Load the naughty strings from a JSON file in the same directory
    with open('blns.json', 'r', encoding='utf-8') as file:
        naughty_strings = json.load(file)

    error_messages = []

    while len(error_messages) < 7:
        val1 = random.choice(naughty_strings + list(range(100)))
        val2 = random.choice(naughty_strings + list(range(100)))

        try:
            func(val1, val2)
        except (ZeroDivisionError, TypeError) as e:
            error_message = f"Error with {val1}/{val2}: {e}"
            error_messages.append(error_message)
            print(error_message)
    pass 

if __name__=='__main__':
    print("Dividing fuzz")
    simpleFuzzer(fuzzValuesDiv)
    print("Adding fuzz")
    simpleFuzzer(fuzzValuesAdd)
    print("Subbing fuzz")
    simpleFuzzer(fuzzValuesSub)
    print("Multiplying fuzz")
    simpleFuzzer(fuzzValuesMult)
    print("Remainding fuzz")
    simpleFuzzer(fuzzValuesRemaind)
    print("Pow fuzz")
    simpleFuzzer(fuzzValuesPow)
    

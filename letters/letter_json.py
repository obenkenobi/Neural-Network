from letters.lettergenerator import generate_h_list
from letters.lettergenerator import generate_l_list
import json

def make_letter_json(num):
    """
    creates a json file of num amount of letter arrays
    where a list for each letter has num/2 arrays
    """
    letter_data = {
        'H': generate_h_list(length=num//2), 
        'L': generate_l_list(length=num//2)
    }
    with open("letters.json", 'w') as f:
        json.dump(letter_data, f, indent=2)

def letter_json_load():
    with open("letters.json", 'r') as f:
        return json.load(f)

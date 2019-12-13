from letters.lettergenerator import generate_h_list
from letters.lettergenerator import generate_l_list
import json

def make_letter_json(num):
    """
    creates a json file of num amount of letter arrays
    where a list for each letter has num/2 arrays.
    The json stores letter data such that the
    key is a letter category and the value 
    is an array of arrays fitting that category
    """
    letter_data = {
        'H': generate_h_list(length=num//2), 
        'L': generate_l_list(length=num//2)
    }
    with open("letters.json", 'w') as f:
        json.dump(letter_data, f, indent=2)

def letter_json_load():
    """
    loads a dictionary from a json file whose key is a letter category 
    and value is an array of arrays fitting that category
    """
    with open("letters.json", 'r') as f:
        return json.load(f)

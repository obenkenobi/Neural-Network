from random import randint
from random import sample

def generate_h():
    """
    generator that generates a random H array
    """
    return [1,0,randint(0,1),1,1,1,randint(0,1),randint(0,1),1,1,0,1]

def generate_l():
    """
    generator that generates a random L array
    """
    return [1,0,0,randint(0,1),0,0,1,0,randint(0,1),1,1,randint(0,1)]

def generate_letter_list(generator, length=300):
    """
    generates a list of letter arrays using a generator function and a defined array length
    """
    letter_list = []
    for i in range(length):
        letter_list.append(generator())
    return letter_list

def generate_h_list(length=300):
    """
    generates a list of H arrays using a generator function and a defined array length
    """
    return generate_letter_list(generate_h, length=length)

def generate_l_list(length=300):
    """
    generates a list of L arrays using a generator function and a defined array length
    """
    return generate_letter_list(generate_l, length=length)

import math
from random import shuffle

def btuple_to_num(bins):
    """
    takes a tuple of 1s and 0s and treats it as a binary number returing
    its decimal equivelent
    """
    exp = 0
    sum = 0
    for val in bins:
        if val != 1 and val != 0:
            raise Exception("Value in bins is not 0 or 1")
        sum+= val*math.pow(2,exp)
        exp += 1
    return int(sum)
    
def list_len_equal(arrs, length):
    """
    returns true if the length of all the lists in arrs
    is equal to length
    """
    for arr in arrs:
        if len(arr) != length:
            return False
    return True

def divisible(num, divisor):
    """
    returns true if num is divisible by divisor,
    else it returns false
    """
    return int(num) % int(divisor) == 0

def shuffled_indexes(length):
    """
    returns a randomly shuffled array whose values
    fall in the range from zero to length
    """
    indexes = list(range(length))
    shuffle(indexes)
    return indexes

def matrix_str(matrix):
    matrix_str = ''
    index = 0
    for row in matrix:
        matrix_str += '\t'+ str(index) +' : '+ str(row) +'\n'
        index += 1
    return matrix_str

def dict_list_str(dict_list):
    string = ''
    for dictionary in dict_list:
        string += '\t'
        for key in dictionary:
            string += str(key) + ': ' + str(dictionary[key]) +', '
        string = string[:-2]
        string += '\n'
    return string
        
    
    
    
    

import math
from mlearn.helper import btuple_to_num
from mlearn.helper import list_len_equal
from mlearn.helper import divisible
from mlearn.helper import shuffled_indexes
from random import randint

class NeuralNetwork:
    def __init__(self):
        self._h_matrix = []
        self._l_matrix = []
        self._s_list = []
    
    @property
    def s_list_len(self):
        return len(self._s_list)
    
    def train(self, h_data, l_data, s_tuple_len=3):
        len_arr = len(h_data[0])
        
        if not list_len_equal(h_data + l_data, len_arr):
            raise Exception("All lists must be of the same length")
        if not divisible(len_arr, s_tuple_len):
            raise Exception("list lengths must be divisible by s_tuple_len")
        
        indexes = shuffled_indexes(len_arr)
        
        # setup s list
        self._s_list = []
        for i in range(0,len_arr,s_tuple_len):
            s_tuple = tuple(indexes[i:i+s_tuple_len])
            self._s_list.append(s_tuple)
        s_list_len = self.s_list_len
            
        # setup matrix columns
        matrix_cols = btuple_to_num([1]*s_tuple_len)+1
        for i in range(matrix_cols):
           self._h_matrix.append([0]*s_list_len)
           self._l_matrix.append([0]*s_list_len)
           
        # storing h data
        for h_arr in h_data:
            for row in range(s_list_len):
                min_index = row*s_tuple_len
                h_tuple = h_arr[min_index:min_index+s_tuple_len]
                h_num = btuple_to_num(h_tuple)
                self._h_matrix[h_num][row] += 1
        
        # storing l data
        for l_arr in l_data:
            for row in range(s_list_len):
                min_index = row*s_tuple_len
                l_tuple = l_arr[min_index:min_index+s_tuple_len]
                l_num = btuple_to_num(l_tuple)
                self._l_matrix[l_num][row] += 1
                

    def predict(self, letter):
        h_sum, l_sum = 0, 0
        s_list_len, s_tuple_len = self.s_list_len, len(self._s_list[0])
        for row in range(s_list_len):
            min_index = row*s_tuple_len
            letter_tuple = letter[min_index:min_index+s_tuple_len]
            letter_num = btuple_to_num(letter_tuple)
            h_sum += self._h_matrix[letter_num][row]
            l_sum += self._l_matrix[letter_num][row]
        if h_sum > l_sum:
            return 'H'
        elif h_sum < l_sum:
            return 'L'
        else:
            return 'H' if randint(0,1) == 0 else 'L'
    
    def test(self, h_data, l_data):
        correct = 0
        for letter in h_data:
            if self.predict(letter) == 'H':
                correct += 1
        for letter in l_data:
            if self.predict(letter) == 'L':
                correct += 1
        return correct/(len(h_data) + len(l_data))

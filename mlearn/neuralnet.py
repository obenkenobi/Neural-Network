import math
from mlearn.helper import btuple_to_num
from mlearn.helper import list_len_equal
from mlearn.helper import divisible
from mlearn.helper import shuffled_indexes
from mlearn.helper import matrix_str
from random import randint
from random import shuffle

class NeuralNetwork:
    """
    Neural network class. This class defines a neural network that categorizes data based on
    two binary categories, 'L' or 'H'. It is initially untrained and must be trained afterwards.
    """
    
    def __init__(self):
        """
        initializes neural network class but doesn't trains it
        """
        self._h_matrix = []
        self._l_matrix = []
        self._s_list = []
    
    @property
    def s_list_len(self):
        return len(self._s_list)
    
    @property
    def h_matrix(self):
        return self._h_matrix.copy()
    
    @property
    def l_matrix(self):
        return self._l_matrix.copy()
    
    @property
    def s_list(self):
        return self._s_list.copy()
    
    def __str__(self):
        return "s list/set:\n"+matrix_str(self.s_list)+"\nH matrix:\n"+matrix_str(self.h_matrix)+"\nL matrix:\n"+matrix_str(self.l_matrix)
    
    def train(self, h_data, l_data, s_tuple_len=3):
        """
        trains the neural network using h_data which is an array of arrays where each array can be classified as 'H',
        the same applies for l_data except the data is classified as l.
        
        s_tuple_len is some value such the length of all the arrays in h_data and l_data is divsible by it.
        This value is used to indicate the how much data is prescribed to a single pattern in our neural network.
        """
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
        """
        predicts what letter the letter array is
        """
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
        """
        Takes testing data, both array of arrays where each array is a letter array and tests how accurate our neural
        network is. It is assumed h_data is classified as 'H' and l_data is classified as 'L'
        """
        results = []
        correct = 0
        
        for letter in h_data:
            letter = letter.copy()
            prediction = self.predict(letter)
            if prediction == 'H':
                letter.append(True)
                correct += 1
            else:
                letter.append(False)
            results.append({'Actual class': 'H', 'Predicted class': prediction, 'array': letter})
        
        for letter in l_data:
            letter = letter.copy()
            prediction = self.predict(letter)
            if prediction == 'L':
                letter.append(True)
                correct += 1
            else:
                letter.append(False)
            results.append({'Actual class': 'L', 'Predicted class': prediction, 'array': letter})
            
            shuffle(results)
            #print(results)
                
        return correct/(len(h_data) + len(l_data)), results

from letters.letter_json import make_letter_json # generates H and L data to a json file
from letters.letter_json import letter_json_load # Loads data from a json file
from mlearn.neuralnet import NeuralNetwork # Neural Network class
from mlearn.helper import dict_list_str # needed to parse a list of dictionaries into a readable string
from random import shuffle # needed to shuffle data
import json 

def print_datalength(h_training, h_testing, l_training, l_testing):
    """
    prints lengths of training and testing data
    """
    print('Data lengths:')
    print('\tH training data length: ', len(h_training))
    print('\tH testing data length: ', len(h_testing))
    print('\tL training data length: ', len(l_training))
    print('\tL testing data length: ', len(l_testing))

tuple_size = input("Insert tuple size that 12 can divide by (default = 3): ") # Prompts user fot tuple size

# Converts and check if input is valid, defaulting to 3 if its wrong
try:
    tuple_size = int(tuple_size)
    if tuple_size <= 0 or 12 % tuple_size > 0:
        raise Exception("tuple size must be greater than 0")
except ValueError as e:
    print("Must input a number, setting tuple size to default size, 3")
    tuple_size = 3
except Exception as e:
    print("Number must be greater than 0 or must be a value 12 is divisable by.")
    print("Setting tuple_size to default size, 3")
    tuple_size = 3
input("Press Enter to continue")
    

make_letter_json(600, filename="letters.json") # randomly generate letter data into a json file called letters.json
letter_data = letter_json_load(filename="letters.json") # load letter data from a json file called letters.json, letter data is a dictionary where key 'L' represents L arrays and 'H' represents H arrays

accuracy_sum = 0 # Sum of all accuracies 
iterations = 100 # total number of iterations
net = NeuralNetwork() # create a neural network object (currently not trained)

# in each iteration, the data will be shuffled and have its accuracy calculated so that the average accuracy is calculated
for i in range(iterations):
    print('---------------------------------------------------------------------------------------------------------------\n')
    print('Neural Network Test '+str(i+1)+'\n')
    print('shuffling data...\n')
    
    #shuffle the data
    shuffle(letter_data['H'])
    shuffle(letter_data['L'])

    # extract training and testing data
    h_training, h_testing, l_training, l_testing = letter_data['H'][:200], letter_data['H'][200:], letter_data['L'][:200], letter_data['L'][200:] # splitting data to be training and testing data for H and L
    
    print_datalength(h_training, h_testing, l_training, l_testing) # prints lendatagth of your training and testing 

    net.train(h_training, l_training, j_tuple_len=tuple_size) # trains the neural network
    accuracy, results = net.test(h_testing, l_testing) # tests the neural network and returns the accuracy and results
    accuracy_sum += accuracy # incrementing sum of accuracies
    print('\n---------------------------\n  Trained neural network  |\n---------------------------\n\n'+str(net))
    print('------------------\n     Results     |\n------------------\n\n'+dict_list_str(results))
    print('accuracy: ',accuracy*100,'%')

avg_accuracy = accuracy_sum/iterations # calculating average accuracy
print('\n---------------------------------------------------------------------------------------------------------------\n')
print('Total tests: '+str(iterations))
print('average accuracy: ', round(avg_accuracy*100, 2),"%")




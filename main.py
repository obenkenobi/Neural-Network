 
from letters.letter_json import make_letter_json
from letters.letter_json import letter_json_load
from mlearn.neuralnet import NeuralNetwork
from mlearn.helper import dict_list_str
from random import shuffle
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

make_letter_json(600, filename="letters.json") # randomly generate letter data into a json file called letters.json
letter_data = letter_json_load(filename="letters.json") # load letter data from a json file called letters.json

accuracy_sum = 0
iterations = 100 
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
    h_training, h_testing, l_training, l_testing = letter_data['H'][:200], letter_data['H'][200:], letter_data['L'][:200], letter_data['L'][200:]
    print_datalength(h_training, h_testing, l_training, l_testing)

    net.train(h_training, l_training) # trains the neural network
    accuracy, results = net.test(h_testing, l_testing) # tests the neural network and returns the accuracy and results
    accuracy_sum += accuracy
    print('\n---------------------------\n  Trained neural network  |\n---------------------------\n\n'+str(net))
    print('------------------\n     Results     |\n------------------\n\n'+dict_list_str(results))
    print('accuracy: ',accuracy*100,'%')

avg_accuracy = accuracy_sum/iterations
print('\n---------------------------------------------------------------------------------------------------------------\n')
print('Total tests: '+str(iterations))
print('average accuracy: ', round(avg_accuracy*100, 2),"%")




 
from letters.letter_json import make_letter_json
from letters.letter_json import letter_json_load
from mlearn.neuralnet import NeuralNetwork
from random import shuffle
#from math import round
import json 

def print_datalength(h_training, h_testing, l_training, l_testing):
    """
    prints lengths of training and testing data
    """
    print('-------------------------------------------')
    print('H training data length: ', len(h_training))
    print('H testing data length: ', len(h_testing))
    print('L training data length: ', len(l_training))
    print('L testing data length: ', len(l_testing))
    print('-------------------------------------------')

make_letter_json(600, filename="letters.json") # randomly generate letter data into a json file called letters.json
letter_data = letter_json_load(filename="letters.json") # load letter data from a json file called letters.json

# print data
#print('training data:')
#print(json.dumps(letter_data, indent=2))

accuracy_sum = 0
iterations = 25 
net = None
h_training, h_testing, l_training, l_testing = None, None, None, None

# in each iteration, the data will be shuffled and have its accuracy calculated so that the average accuracy is calculated
for i in range(iterations):

    #shuffle the data
    shuffle(letter_data['H'])
    shuffle(letter_data['L'])

    # extract training and testing data
    h_training, h_testing, l_training, l_testing = letter_data['H'][:200], letter_data['H'][200:], letter_data['L'][:200], letter_data['L'][200:]

    net = NeuralNetwork() # create a neural network object (currently not trained and setup)
    net.train(h_training, l_training) # trains the neural network
    accuracy = net.test(h_testing, l_testing) # gets the accurracy of the neural network
    accuracy_sum += accuracy
    print('-------------------------------------------')
    print('Neural Network: '+str(i+1)+'\n')
    print(net)
    print('accuracy: ',accuracy*100,'%')

print_datalength(h_training, h_testing, l_training, l_testing)
avg_accuracy = accuracy_sum/iterations
print('Tests = '+str(iterations))
print('average accuracy: ', round(avg_accuracy*100, 2),"%")




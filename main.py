 
from letters.letter_json import make_letter_json
from letters.letter_json import letter_json_load
from mlearn.neuralnet import NeuralNetwork
from random import shuffle
import json 

make_letter_json(600, filename="letters.json") # generate letter data into a json file called letters.json
letter_data = letter_json_load(filename="letters.json") # load letter data from a json file called letters.json

# print data
#print('training data:')
#print(json.dumps(letter_data, indent=2))

#shuffle the data
shuffle(letter_data['H'])
shuffle(letter_data['L'])

# extract training and testing data
h_training, h_testing, l_training, l_testing = letter_data['H'][:200], letter_data['H'][200:], letter_data['L'][:200], letter_data['L'][200:]

print('H training data length: ', len(h_training))
print('H testing data length: ', len(h_testing))
print('L training data length: ', len(l_training))
print('L testing data length: ', len(l_testing))

net = NeuralNetwork() # create a neural network object (currently not trained and setup)
net.train(h_training, l_training) # trains the neural network
accuracy = net.test(h_testing, l_testing) # gets the accurracy of the neural network
print('accuracy: ', accuracy*100,"%")




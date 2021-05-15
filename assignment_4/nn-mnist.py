#!/usr/bin/env python

# Importing libraries
import sys, os, argparse, joblib, cv2
sys.path.append(os.path.join(".."))
import utils.classifier_utils as clf_util
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn import datasets
from sklearn.datasets import fetch_openml
from utils.neuralnetwork import NeuralNetwork
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

# Define function for loading and splitting the MNIST dataset
def load_split_MNIST():
    # Importing data; y = what the image depicts, X = values for all pixels (from top right, moving left)
    print("[INFO] Loading the MNIST dataset ...")
    X, y = fetch_openml('mnist_784', version = 1, return_X_y = True)

    # Converting to numpy arrays
    X = np.array(X)
    y = np.array(y)
    
    # Make a test-train split of some of the data
    X_train, X_test, y_train, y_test = train_test_split(X, 
                                                        y, 
                                                        random_state = 9, # for replication purposes
                                                        train_size = 20000, # absolute size of test and train set to avoid too much data
                                                        test_size = 2000)

    # Return X and y
    return X_train, X_test, y_train, y_test

# Define function for min max scaling
def min_max_scaling(X_train, X_test):
    # Min-max scaling:
    scaler = MinMaxScaler()
    scaler = scaler.fit(X_train) # Important to scale not only train data but also test data information from train
    X_train_scaled = pd.DataFrame(scaler.transform(X_train))
    X_test_scaled = pd.DataFrame(scaler.transform(X_test))
    
    # Return scaled values
    return X_train_scaled, X_test_scaled, scaler

# Define function for binarizing labels
def binarize_labels(y_train, y_test):
    # Binarize the labels (getting from e.g. [3,1,2] to [[0,0,1],[1,0,0],[0,1,0], instead of course with numbers from 0-10) 
    y_train = LabelBinarizer().fit_transform(y_train) 
    y_test = LabelBinarizer().fit_transform(y_test)
    
    # Return binarized labels
    return y_train, y_test

# Define function for training neural network with set parameters
def train_nn(X_train_scaled, y_train, hiddenlayers, epochs):
    # Assigning more layers in the neural network:
    hiddenlayers.insert(0, X_train_scaled.shape[1]) # Inserting the number of features as the input layer
    hiddenlayers.append(10) # Inserting the number of possible outcomes as the output layer
    
    # Defining a model (with the specified number of nodes and layers)
    nn = NeuralNetwork(hiddenlayers)
    
    # Fit the model to the training data
    print("[INFO] Training the neural networks classifier ...") # Information for terminal use
    nn.fit(X_train_scaled, y_train, epochs = epochs)
    
    # Return the model
    return nn

# Define function for getting performance metrics
def get_performance(save, outname, nn, X_test_scaled, y_test):
    # Using the fitted model to predict the test data
    predictions = nn.predict(X_test_scaled)

    # The "predictions" object contains certainties that the given image contains a 0, 1, 2, etc. Instead we want a single prediction
    predictions = predictions.argmax(axis=1)
    
    # Getting a classification report:
    print("[INFO] Evaluating the neural networks classifier ...") # Information for terminal use
    classif_report = pd.DataFrame(classification_report(y_test.argmax(axis=1), predictions, output_dict = True, digits = 3))

    # Print to terminal
    print(classif_report)

    # Save classification report as csv in "out"-folder and save the model, if save == True
    if save == True:
        # If the folder does not already exist, create it
        if not os.path.exists("out"):
            os.makedirs("out")
            
        # Saving classification report
        outpath_classif_report = os.path.join("out", outname)
        classif_report.to_csv(outpath_classif_report, index = True)
        print(f"[INFO] The classification benchmark report has been saved: \"{outpath_classif_report}\".")
        
        # Saving model
        outpath_nn_model = os.path.join("out", "nn_model.pkl")
        joblib.dump(nn, outpath_nn_model)
        print(f"[INFO] The trained neural networks model has been saved: \"{outpath_nn_model}\".")

# Define function for prediction individual image from trained model
def pred_individual(individual, nn, y_train, scaler):
    # Read individual image and convert to grayscale
    image = cv2.imread(individual)
    gray = cv2.bitwise_not(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))

    # Compress image to fit the input size of the model 
    compressed = cv2.resize(gray, (28, 28), interpolation=cv2.INTER_AREA)

    # Flatten the compressed image (converting a list of lists into a list)
    compressed_flattened = [float(item) for sublist in compressed for item in sublist] 

    # Converting the flattened compressed image to array
    compressed_flattened = np.array(compressed_flattened)

    # Scaling the features of the individual image
    compressed_flattened = pd.DataFrame(scaler.transform([compressed_flattened]))

    # Predicting the individual image (output = 10 probabilities - one for each class (0:9)). Using the highest probability as the prediction
    individual_pred = nn.predict(compressed_flattened)
    individual_pred = int(individual_pred.argmax(axis=1))
    print(f"[IMAGE PREDICTION] Image prediction for \"{individual}\": {individual_pred}") # Printing into terminal, the prediction
    
# Defining main function
def main(outname, save, individual, hiddenlayers, epochs):
    # Load MNIST dataset and split it
    X_train, X_test, y_train, y_test = load_split_MNIST()
    
    # Min-max scale the X-values
    X_train_scaled, X_test_scaled, scaler = min_max_scaling(X_train, X_test)
    
    # Binarize labels
    y_train, y_test = binarize_labels(y_train, y_test)
    
    # Train a neural networks classifier, with parameters "hiddenlayers" and "epochs"
    nn = train_nn(X_train_scaled, y_train, hiddenlayers, epochs)
    
    # Get performance - and if save == True, then save performance
    get_performance(save, outname, nn, X_test_scaled, y_test)
    
    # If the argument for individual prediction is not "None", then predict the individual image
    if individual != None:
        pred_individual(individual, nn, y_train, scaler)

# Define behaviour when called from command line
if __name__=="__main__":
    # Initialize ArgumentParser class
    parser = argparse.ArgumentParser(
        description = "[SCRIPT DESCRIPTION] Script that trains a neural networks classifier on a subset of the mnist dataset. Tests on another part of the mnist dataset and outputs classification report. Number and depth of hidden layers can be specified using the -hiddenlayers argument. The trained model can also be used to predict individual images, using the argument --individual.") 

    # Add argument specifying name of classification report
    parser.add_argument(
        "-o",
        "--outname",
        type = str,
        default = "classif_report_neural_networks.csv", # Default when not specifying name of outputfile
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "str - containing name of classification report")

    # Add argument specifying whether we want the classification report saved
    parser.add_argument(
        "-s",
        "--save", 
        type = bool,
        default = True, # Default when not specifying 
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "bool - specifying whether to save classification report")

    # Add argument specifying an individual image that is wanted predicted
    parser.add_argument(
        "-i",
        "--individual", 
        type = str,
        default = os.path.join("data", "test.png"), # Default when not specifying anything in the terminal
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "str - specifying a .png file which is to be classified using this neural networks model.")

    # Add argument specifying the hidden layers
    parser.add_argument(
        "-H",
        "--hiddenlayers", 
        type = list,
        default = [16, 8], # Default when not specifying anything in the terminal
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "list - specifying the hidden layers, each element in the list corresponds to number of nodes in layer. index in list corresponds to hiddenlayer number. E.g. [32, 16]")
    
    # Add argument specifying number of epochs
    parser.add_argument(
        "-e",
        "--epochs", 
        type = int,
        default = 200, # Default when not specifying anything in the terminal
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "int - specifying number of epochs for training the model.")
    
    # Taking all the arguments we added to the parser and input into "args"
    args = parser.parse_args()

    # Execute main function
    main(args.outname, args.save, args.individual, args.hiddenlayers, args.epochs)

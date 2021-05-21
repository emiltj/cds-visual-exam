#!/usr/bin/env python

############### Importing libraries ################
# data tools
import os, cv2, glob, argparse
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# sklearn tools
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report

# tf tools
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import plot_model
from tensorflow.keras.optimizers import SGD
from tensorflow.keras import backend as K
from tensorflow.keras.layers import (Conv2D, 
                                     MaxPooling2D, 
                                     Activation, 
                                     Flatten, 
                                     Dense)

############### Defining functions to be used in main ###############
def get_artists(artists_path):
    """
    Function which retrieves an alphabetically sorted artists list.
    
    artists_path: Path to folder containing all folders with artists
    """
    artists = os.listdir(artists_path) # Get list of directories (each names corresponds to artists' names
    artists = sorted(artists) # Sort alphabetically
    return artists

def get_train_test(artists):
    """
    Function which retrieves the train/test data from the folder structure.
    
    artists: list of names of artists
    """
    # Make empty lists, which are to be appended to
    train_paintings, train_paintings_artists = [], []
    test_paintings, test_paintings_artists = [], []

    # For every artist, generate a list of paintings. 
    # For every painting in list of paintings, take the artist name and append it to the list. Take the painting name and append it also
    # Repeat for testing data
    for artist in artists:
        print(f"[INFO] Importing paintings from: {artist}") # Information for user in terminal
        # Training
        for train_painting in glob.glob(os.path.join("data", "training", f"{artist}", "*.jpg")):
            train_paintings_artists.append(artist)
            train_paintings.append(cv2.imread(train_painting))
        # Testing
        for test_painting in glob.glob(os.path.join("data", "validation", f"{artist}", "*.jpg")):
            test_paintings_artists.append(artist)
            test_paintings.append(cv2.imread(test_painting))
    
    # Return the lists
    return train_paintings, train_paintings_artists, test_paintings, test_paintings_artists

def get_resized_arrays(paintings, width, height): 
    """
    Function which resizes images to argument dimensions and makes them into np.arrays.
    
    paintings: list of arrays/paintings
    width: wanted width after using the function
    height: wanted height after using the function
    """
    # Empty list for appending to
    paintings_resized = []
    
    # For every painting in the list of paintings
    for painting in paintings:
        # Resize painting
        resized = cv2.resize(painting, (width, height), interpolation = cv2.INTER_AREA)
        
        # Normalize painting
        resized = resized.astype("float") / 255.
        
        # Append to list
        paintings_resized.append(resized)
    
    # Make into arrays with same dimensions instead of lists
    paintings_resized = np.array(paintings_resized).reshape(len(paintings_resized), width, height, 3)
    
    # Return
    return paintings_resized

def plot_history(H, epochs, cnn):
    """
    Function which plots accuracy and loss over epochs (courtesy of Ross McLachlan).
    
    H: History of the model
    epochs: Number of epochs
    cnn: Name of cnn architecture
    """
    # Visualizing performance
    plt.style.use("fivethirtyeight")
    plt.figure()
    plt.plot(np.arange(0, epochs), H.history["loss"], label="train_loss")
    plt.plot(np.arange(0, epochs), H.history["val_loss"], label="val_loss")
    plt.plot(np.arange(0, epochs), H.history["accuracy"], label="train_acc")
    plt.plot(np.arange(0, epochs), H.history["val_accuracy"], label="val_acc")
    plt.title("Training Loss and Accuracy")
    plt.xlabel("Epoch #")
    plt.ylabel("Loss/Accuracy")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join("out", f'{cnn}_training_history.png'), format='png', dpi=100)

############### Defining main function ###############
def main(cnn, resizedim,  batchsize, epochs):
    """
    Main function.
    
    cnn: Name of cnn architecture
    resizedim: Dimensions to resize to
    batchsize: Batch size for training
    epochs: Number of epochs
    """
    # Make a alphabetically sorted list of all the artists
    artists_path = os.path.join("data", "training")
    artists = get_artists(artists_path)

    # Get the data we need
    train_paintings, train_paintings_artists, test_paintings, test_paintings_artists = get_train_test(artists)

    # Resize and make into arrays (and give proper name)
    trainX = get_resized_arrays(train_paintings, resizedim[0], resizedim[1])
    testX = get_resized_arrays(test_paintings, resizedim[0], resizedim[1])

    # Binarize labels
    lb = LabelBinarizer()
    trainY = lb.fit_transform(train_paintings_artists)
    testY = lb.fit_transform(test_paintings_artists)

    # Initialize label names
    labelNames = artists # Here we know that the order is the same in "artists", so we know how to map the binarized labels onto the string names
    
    # If we're using the ShallowNet architecture
    if cnn == "ShallowNet":
        architecture = "INPUT => CONV => ReLU => FC"
        # initialise model
        model = Sequential()

        # define CONV => RELU layer
        model.add(Conv2D(32, (3, 3),
                         padding="same", 
                         input_shape=(32, 32, 3)))
        model.add(Activation("relu"))

        # softmax classifier
        model.add(Flatten())
        model.add(Dense(10))
        model.add(Activation("softmax"))
    
    # Else, if we're using the LeNet architecture
    elif cnn == "LeNet":
        architecture = "INPUT => CONV => ReLU => MAXPOOL => CONV => ReLU => MAXPOOL => FC => ReLU => FC"
        # define model
        model = Sequential()

        # first set of CONV => RELU => POOL
        model.add(Conv2D(32, (3, 3), 
                         padding="same", 
                         input_shape=(32, 32, 3)))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), 
                               strides=(2, 2)))

        # second set of CONV => RELU => POOL
        model.add(Conv2D(50, (5, 5), 
                         padding="same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), 
                               strides=(2, 2)))

        # FC => RELU
        model.add(Flatten())
        model.add(Dense(500))
        model.add(Activation("relu"))

        # softmax classifier
        model.add(Dense(10))
        model.add(Activation("softmax"))

    # Define step size for the gradient descent, as well as define the loss function
    opt = SGD(lr =.01)
    model.compile(loss="categorical_crossentropy",
                  optimizer=opt,
                  metrics=["accuracy"])

    print("Commencing model fitting")
    # Fit the model
    H = model.fit(trainX, trainY, 
                  validation_data=(testX, testY), 
                  batch_size = batchsize,
                  epochs = epochs)#,
                  #verbose = 1) # Showing the training the terminal
    
    # Information for the user in terminal
    print(f"[INFO] Training of the model has been completed using a batchsize of {batchsize} and using the CNN architecture from {cnn}: \n {architecture}\n")

    # Get predictions:
    predictions = model.predict(testX, batch_size = batchsize)

    # Get classification report from predictions
    classif_report = pd.DataFrame(classification_report(testY.argmax(axis=1),
                                predictions.argmax(axis = 1),
                                target_names = labelNames, output_dict = True))

    # If the folder does not already exist, create it
    if not os.path.exists("out"):
        os.makedirs("out")
        
    # Printing and saving classification_report
    print(classif_report)
    classif_report_outname = os.path.join("out", f'{cnn}_classification_report.csv')
    classif_report.to_csv(classif_report_outname, sep=',', index = True)
    print(f"A classification report has been saved succesfully: \"{classif_report_outname}\"")

    # Show plot of accuracy and loss over epochs and save it
    plot_history(H, epochs, cnn)
    print(f"A plot history report has been saved succesfully: \"out/{cnn}_training_history.png\"")

    # Show the model architecture and save it
    model_plot_outname = os.path.join("out", f'{cnn}_model_plot.png')
    plot_model(model, to_file = model_plot_outname, show_shapes=True, show_layer_names=True)
    print(f"A visualization of the CNN model architecture has been saved succesfully: \"{model_plot_outname}\"")

############### Defining use when called from terminal ################
if __name__=="__main__":
    # Initialise ArgumentParser class
    parser = argparse.ArgumentParser(description = "[SCRIPT DESCRIPTION] Script that trains a convolutional neural network on impressionist paintings and tests on an unseen part of the same data set. ")
    
    # Add inpath argument
    parser.add_argument(
        "-c",
        "--cnn", 
        type = str,
        default = "ShallowNet",
        required = False,
        help = "str - specifying cnn architecture, use either \"ShallowNet\" or \"LeNet\"")
    
    # Add outpath argument
    parser.add_argument(
        "-r",
        "--resizedim",
        type = list, 
        default = [32, 32],
        required = False,
        help = "list - specifying dimensions that the pictures should be resized to, e.g. [32, 32]")
        
    # Add batch size argument
    parser.add_argument(
        "-b",
        "--batchsize",
        type = int, 
        default = 200,
        required = False,
        help = "int - specifying batch size")
    
    # Add epochs argument
    parser.add_argument(
        "-e",
        "--epochs",
        type = int, 
        default = 50,
        required = False,
        help = "int - specifying number of epochs")
    
    # Taking all the arguments we added to the parser and input into "args"
    args = parser.parse_args()

    # Execute main function
    main(args.cnn, args.resizedim, args.batchsize, args.epochs)

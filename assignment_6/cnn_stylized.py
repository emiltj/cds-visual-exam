#!/usr/bin/env python

'''
###############################################################
--------------- Import of modules and libraries ---------------
###############################################################
'''
# data tools
import os, cv2, glob, argparse
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# sklearn tools
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder

# tf tools
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import Model
from tensorflow.keras.utils import plot_model
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.keras import backend as K
from tensorflow.keras.layers import (Conv2D,
                                     MaxPool2D,
                                     MaxPooling2D, 
                                     Activation, 
                                     Flatten,
                                     Dropout,
                                     Dense)
from tensorflow.keras.preprocessing.image import (load_img,
                                                  img_to_array,
                                                  ImageDataGenerator)
from tensorflow.keras.applications.vgg16 import (preprocess_input,
                                                 decode_predictions,
                                                 VGG16)


'''
###############################################################
------------ Defining functions to be used in main ------------
###############################################################
'''
def read_from_folders(folders):
    """
    Function which reads images from a list of folders, as well as generates a label, based on the folder names. 
    Returns a data frame with all the information.
    
    Folders: List of paths to folders where images reside
    """
    # Initialize empty lists for appending to
    arrays = []
    labels = []
    
    # For each folder in list of folders
    for folder in folders:
        
        # Get folderpath
        folderpath = os.path.join("data", folder)
        print(f"[INFO] Loading images from: \"{folderpath}\" ...") # Info for terminal
        
        # For each file within the path, append arrays and labels
        for file in glob.glob(os.path.join(folderpath, "*.jpg")):
            arrays.append(cv2.imread(file))
            labels.append(f"{os.path.split(folderpath)[1]}")
    
    # Create dataframe from labels and arrays
    df = pd.DataFrame.from_dict({"X" : arrays, "y" : labels})
    
    # Return the dataframe
    return df

def get_resized_arrays(arrays, width, height):
    """
    Function which resizes arrays to input dimensions - also scales arrays to be between 0 and 1.
    
    Arrays: List of arrays to resize
    Width: Width to resize to
    Height: Height to resize to
    """
    # Info for terminal use
    print("[INFO] Resizing images to match CNN input dimensions ...")
    
    # If pd.series, convert to list
    if type(arrays) == "pandas.core.series.Series":
        arrays = list(arrays)
    
    # Empty list for appending to
    arrays_resized = []
    
    # For every array in the list of arrays
    for array in arrays:
        # Resize array
        resized = cv2.resize(array, (width, height), interpolation = cv2.INTER_AREA)
        
        # Convert to array and values between 0 and 1 to allow to be used in CNN (using list comprehension)
        resized = np.asarray(resized/255.).astype("float32")

        # Append to list
        arrays_resized.append(resized)

    # Return
    return arrays_resized

def get_formatted(X, y):
    """
    Function that formats arrays and labels to be usable in the CNN.
    
    X: List of arrays
    y: List of labels for arrays
    """
    # If pd.series, convert to list
    if type(X) == "pandas.core.series.Series":
        X = list(X)
    if type(y) == "pandas.core.series.Series":
        y = list(y)
        
    # Format X
    X = np.array(X).reshape(len(X), 224, 224, 3)
    
    # Format y to one-hot encoding
    lb, enc = LabelEncoder(), OneHotEncoder()
    y = lb.fit_transform(y).reshape(-1,1)
    y = enc.fit_transform(y).toarray()
    
    # Return the transformed X and y
    return X, y

def plot_history(H, epochs, save):
    """
    Function which plots accuracy and loss over epochs.
    
    H: History of model training
    epochs: Number of epochs
    save: Whether to save the model performance metrics or not
    """
    # Make a list of epochs
    epochs_range = range(epochs)
    
    # Create a plot showing accuracies
    plt.figure(figsize = (15, 15))
    plt.subplot(2, 2, 1)
    plt.plot(epochs_range, H.history['accuracy'], label = 'Training accuracy')
    plt.plot(epochs_range, H.history['val_accuracy'], label = 'Validation accuracy')
    plt.legend(loc = 'lower right')
    plt.title('Training and Validation Accuracy')

    # Create a plot showing loss
    plt.subplot(2, 2, 2)
    plt.plot(epochs_range, H.history['loss'], label = 'Training loss')
    plt.plot(epochs_range, H.history['val_loss'], label = 'Validation loss')
    plt.legend(loc = 'upper right')
    plt.title('Training and Validation Loss')
    
    #Save plot
    if save == True:
        plt.savefig(os.path.join("out", 'training_history.png'), format = 'png', dpi = 100)
    
    plt.show()

def get_classif_report(model, X_test, y_test, label_names, save, outname):
    '''
    Function for retrieving and potentially saving a classification report.
    
    model: Trained model
    X_test: Features/arrays for test
    y_test: Labels for the test set
    label_names: Names of labels
    save: Bool specifying whether to save classification report or not
    outname: Name of file to be saved
    '''
    # Make predictions
    predictions = model.predict(X_test, batch_size = 32)
    
    # Create classification report
    classif_report = pd.DataFrame(classification_report(y_test.argmax(axis = 1), # Take the maximum probability prediction
                                predictions.argmax(axis = 1),
                                target_names = label_names, output_dict = True)) # Labels for classification report should be "label_names"
    
    # Create outpath if it does not already exist
    if not os.path.exists("out"):
        os.makedirs("out")
    
    # Print classification report
    print(classif_report)
    
    # Save classification report
    if save == True:
        classif_report_outpath = os.path.join("out", f'{outname}')
        classif_report.to_csv(classif_report_outpath, sep = ',', index = True)
        print(f"A classification report has been saved succesfully: \"{classif_report_outpath}\"")


'''
###############################################################
---------- Defining the main function of the script -----------
###############################################################
'''
def main(datapath, epochs, save):
    '''
    Defining main function.
    
    datapath: Path to data to classify on
    epochs: Number of epochs for training
    save: Bool specifying whether to save performance metrics or not
    '''
    # Load data
    df = read_from_folders(os.listdir(datapath))

    # Resize arrays to size
    df["X"] = get_resized_arrays(df["X"], 224, 224)

    # Data only from the original paintings, with less complicated labels
    df_orig = df.loc[(df['y'] == "content_monet_style_monet") | (df['y'] == "content_cezanne_style_cezanne")]
    df_orig = df_orig.replace({'y' : { 'content_monet_style_monet' : "monet",
                                      'content_cezanne_style_cezanne' : "cezanne"}})

    # Data only from the stylized paintings, with less complicated labels.
    # NOTE: Monet content Cezanne style paintings are called Monet! And vice versa!
    df_stylized = df.loc[(df['y'] == "content_monet_style_cezanne") | (df['y'] == "content_cezanne_style_monet")]
    df_stylized = df_stylized.replace({'y' : { 'content_monet_style_cezanne' : "monet",
                                              'content_cezanne_style_monet' : "cezanne"}})

    # Get label_names (for classification report)
    label_names = set(df_orig["y"])

    # Define X and y for both original and stylized (formatted to match expected input for CNN)
    X_orig, y_orig = get_formatted(list(df_orig["X"]), list(df_orig["y"]))
    X_stylized, y_stylized = get_formatted(list(df_stylized["X"]), list(df_stylized["y"]))

    # Define the model
    base_model = tf.keras.applications.MobileNetV2(input_shape = (224, 224, 3), # Importing MobileNetV2
                                                   include_top = False,
                                                   weights = "imagenet")
    base_model.trainable = False # Refrain from training the pretrained weights
    model = tf.keras.Sequential([base_model, # Add layers to the pre-trained model
                                     tf.keras.layers.GlobalAveragePooling2D(),
                                     tf.keras.layers.Dropout(0.2), # Dropout layers; randomly drops weights through training (good to avoid overfitting)
                                     tf.keras.layers.Dense(2, activation="softmax")])
    model.compile(optimizer=tf.keras.optimizers.Adam(lr = 0.001), # Compile model
                  loss=tf.keras.losses.BinaryCrossentropy(from_logits = True), # Binary classification
                  metrics=['accuracy'])

    # Save model architecture
    if save == True:
        model_plot_outname = os.path.join("out", 'cnn_architecture.png')
        plot_model(model, to_file = model_plot_outname, show_shapes=True, show_layer_names=True)
        print(f"A visualization of the CNN model architecture has been saved succesfully: \"{model_plot_outname}\"")

    # Make a train-test split of the original data
    X_train, X_test, y_train, y_test = train_test_split(X_orig, 
                                                        y_orig, 
                                                        random_state = 9, # for replication purposes
                                                        train_size = .8)

    # Fit the model to the original data
    history = model.fit(X_train, y_train, 
                  validation_data = (X_test, y_test), 
                  batch_size = 32,
                  epochs = epochs)

    # Plot the training history
    plot_history(history, epochs, save)

    # Predict the original test set
    get_classif_report(model, X_test, y_test, label_names, save, "classification_report_original.csv")

    # Predict the stylized set
    get_classif_report(model, X_stylized, y_stylized, label_names, save, "classification_report_generated.csv")

'''
###############################################################
----------- Defining use when called from terminal ------------
###############################################################
'''
if __name__=="__main__":
    # Initialize ArgumentParser class
    parser = argparse.ArgumentParser(
        description = "[SCRIPT DESCRIPTION] Script that uses a pretrained CNN to classify between Monet and Cezanne paintings. Is tested on a subset and on the newly generated stylized paintings. Saves classification reports and training history.") 

    # Add outname argument
    parser.add_argument(
        "-d",
        "--datapath",
        type = str,
        default = "data", # Default when not specifying name of outputfile
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "str - containing folderpath to parent data folder.")

    # Add individual image prediction argument
    parser.add_argument(
        "-e",
        "--epochs", 
        type = int,
        default = 10, # Default when not specifying anything in the terminal
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "int - specifying number of epochs for re-training the trainable layers of the cnn.")
    
    # Add save argument
    parser.add_argument(
        "-s",
        "--save", 
        type = bool,
        default = True, # Default when not specifying anything else
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "bool - specifying whether to save classification reports")

    # Taking all the arguments we added to the parser and input into "args"
    args = parser.parse_args()
    
    # Execute main function
    main(args.datapath, args.epochs, args.save)

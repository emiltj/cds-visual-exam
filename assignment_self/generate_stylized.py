#!/usr/bin/env python

############### Importing libraries ################
# base tools
import os, sys, random, cv2, glob, argparse
random.seed(14)
sys.path.append(os.path.join(".."))

# Ross' function for showing imgs
from utils.imutils import jimshow

# data analysis
import numpy as np
from PIL import Image
from numpy.linalg import norm
from tqdm import tqdm

# tensorflow
import tensorflow_hub as hub
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input

# style utils
from utils.styletransfer import *

# matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#%matplotlib inline

# Load TF-Hub module.
hub_handle = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
hub_module = hub.load(hub_handle)

############### Defining functions to be used in main ###############
def file_load_random(files):
    """
    Function which loads files from a directory and shuffles the order
    """
    # Info for terminal use
    print(f"[INFO] Loading files: \"{files}\" ...")
    
    # Empty list for appending to
    loaded_imgs = []
        
    # For every filename in the path, st_load
    for filename in glob.glob(files):
        # Append to list
        loaded_imgs.append(st_load(filename))
    
    # Shuffle order
    random.shuffle(loaded_imgs)
    
    # Return randomly shuffled, loaded images
    return loaded_imgs

def get_stylized(imgs_a, imgs_b):
    """
    Function which generates stylized images. Takes two arguments; imgs_a (list) and imgs_b (also list). Outputs the two lists of images, with each others style.
    """
    # Info for terminal use
    print(f"[INFO] Generating stylized images (this may take a while) ...")
    
    # Empty lists for appending to
    content_a_style_b = []
    content_b_style_a = []
    
    # For every image pair
    for a, b in zip(imgs_a, imgs_b):
        
        # Generated stylized images (as np.asarrays)
        content_a_style_b.append(hub_module(a, b)[0]) # First argument is content image, second is style
        content_b_style_a.append(hub_module(b, a)[0])

    # Return them
    return content_a_style_b, content_b_style_a

def preprocess(imgs):
    """
    Function that preprocesses a list of images; returns images as arrays and converts from BGR to RGB.
    """
    # Empty list for appending to
    preprocessed = []
    
    # For every image
    for i in imgs:
        
        # Get i as np.array and only keep the 3 dimensions, height, width, color
        i = np.asarray(i)[0]
        
        # Convert to RGB instead of BGR
        i = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
        
        # Convert to have values between 255 and 0, instead of between 0 and 1 (to allow for using cv2.imwrite)
        i = i*255
        
        # Append to list
        preprocessed.append(i)
    
    # Return preprocessed imgs
    return preprocessed

def save_examples(content_img, style_img, stylized_img, unique_ending):
    """
    Function that saves a set of content, style and stylized images.
    """
    # Create outpath if it does not exist
    if not os.path.exists("out"):
        os.mkdir("out")

    # Define outpath
    example_outpath = os.path.join("out", f"example_{unique_ending}.jpg")
    
    # Creating borders, making it easier to distinguish border around the concatenated images
    content_img = cv2.copyMakeBorder(content_img, 0, 10, 10, 10, cv2.BORDER_CONSTANT) # Creating a border of 10 pixels on all edges except for top.
    style_img = cv2.copyMakeBorder(style_img, 0, 10, 10, 10, cv2.BORDER_CONSTANT)
    stylized_img = cv2.copyMakeBorder(stylized_img, 0, 10, 10, 10, cv2.BORDER_CONSTANT)
        
    # Concatenate images
    example = np.concatenate((content_img, style_img), axis=0)
    example = np.concatenate((example, stylized_img), axis=0)
    
    example = cv2.copyMakeBorder(example, 10, 0, 0, 0, cv2.BORDER_CONSTANT) # Creating a top edge
    
    # Write images
    cv2.imwrite(example_outpath, example)
    
def save_imgs(imgs, outfolder):
    """
    Function which saves a list of images to a given outfolder with unique names. Also creates the outfolder if it does not already exist.
    """
    # Info for terminal use
    print(f"[INFO] Saving stylized images to \"{outfolder}\" ...")
    
    # Initialize counter for unique names
    counter = 0
    
    # Create outpath if it does not exist
    if not os.path.exists(outfolder):
        os.mkdir(outfolder)
    
    # Saving stylized images
    for i in imgs:
        
        # Get unique filename ending
        counter += 1
        
        # Define outpath and save
        outpath = os.path.join(outfolder, f"img_{counter}.jpg")
        cv2.imwrite(outpath, i)
    
    # Info for terminal use
    print(f"[INFO] Stylized images have been saved to \"{outfolder}\" successfully")
    
############### Defining main function ###############
def main(inpath_a, inpath_b, outpath_content_a_style_b, outpath_content_b_style_a):
    """
    Main function.
    """
    # Loading files
    a = file_load_random(inpath_a)
    b = file_load_random(inpath_b)
    
    # Generate stylized images
    content_a_style_b, content_b_style_a = get_stylized(a, b)
    
    # Preprocess images
    print(f"[INFO] Preprocessing stylized images ...") # Info for terminal use
    a = preprocess(a)
    b = preprocess(b)
    content_a_style_b = preprocess(content_a_style_b)
    content_b_style_a = preprocess(content_b_style_a)
       
    # Save a few examples
    print("[INFO] Saving examples of stylized images to \".out/\" ...") # Info for terminal use
    for i in range(10):
        save_examples(a[i], b[i], content_a_style_b[i], f"{i}")

    for i in range(10):
        save_examples(b[i], a[i], content_b_style_a[i], f"{i+10}")
    
    # Save all newly stylized paintings
    save_imgs(content_a_style_b, outpath_content_a_style_b)
    save_imgs(content_b_style_a, outpath_content_b_style_a)

############### Defining use when called from terminal ################
if __name__=="__main__":
    # Initialize ArgumentParser class
    parser = argparse.ArgumentParser(description = "[SCRIPT DESCRIPTION] Generates two sets of stylized images from two corpora. It pairs images from the two corpora randomly, and generates two new stylized images per pair. One with content of image a and style of image b, and vice versa.")
    
    # Add inpath a argument
    parser.add_argument(
        "-i",
        "--inpatha", 
        type = str,
        default = os.path.join("data", "content_gauguin_style_gauguin", "*.jpg"), # Default path to corpus, when none is specified
        required = False,
        help= "str - path to image corpus a")
    
    # Add inpath b argument
    parser.add_argument(
        "-I",
        "--inpathb",
        type = str,
        default = os.path.join("data", "content_monet_style_monet", "*.jpg"), # Default path to corpus, when none is specified
        required = False,
        help= "str - path to image corpus b")
    
    # Add inpath b argument
    parser.add_argument(
        "-o",
        "--outpatha",
        type = str,
        default = os.path.join("data", "content_gauguin_style_monet"), # Default path to corpus, when none is specified
        required = False,
        help= "str - path to output path of the stylized images with content_a_style_b")
    
    # Add inpath b argument
    parser.add_argument(
        "-O",
        "--outpathb",
        type = str,
        default = os.path.join("data", "content_monet_style_gauguin"), # Default path to corpus, when none is specified
        required = False,
        help= "str - path to output path of the stylized images with content_b_style_a")
    
    # Taking all the arguments we added to the parser and input into "args"
    args = parser.parse_args()
    
    # Perform main function
    main(args.inpatha, args.inpathb, args.outpatha, args.outpathb)

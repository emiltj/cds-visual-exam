# base tools
import os, sys, random, cv2, glob, argparse
random.seed(11)
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

# Defining function for loading files
def file_load_random(files):
    # Info for terminal use
    print(f"[INFO] Loading files from \"{files}\" ...")
    
    # Empty list for appending to
    loaded = []
    
    #loaded = loaded[:10]
    
    # For every filename in the path, st_load
    for filename in glob.glob(files):
        loaded.append(st_load(filename))
    
    # Shuffle order
    random.shuffle(loaded)
    
    # Return randomly shuffled, loaded images
    return loaded

# Defining function for generating stylized images
def get_stylized(imgs_a, imgs_b):
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
    
# Define function for preprocessing
def preprocess(imgs):
    # Info for terminal use
    print(f"[INFO] Preprocessing stylized images ...")
    
    # Empty list for appending to
    preprocessed = []
    
    # For every image
    for i in imgs:
        
        # Get i as np.array and only keep the 3 dimensions, height, width, color
        i = np.asarray(i)[0]
        
        # Convert to RGB instead of BGR
        i = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
        #i[:,:,::-1]
        
        # Convert to have values between 255 and 0, instead of between 0 and 1 (to allow for using cv2.imwrite)
        i = i*255
        
        # Append to list
        preprocessed.append(i)
    
    # Return preprocessed imgs
    return preprocessed

# Define function for saving the stylized images
def save_imgs(imgs, outfolder):
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
    
# Defining main function
def main(inpath_a, inpath_b, outpath_content_a_style_b, outpath_content_b_style_a):
    
    # Loading files
    a = file_load_random(inpath_a)
    b = file_load_random(inpath_b)
    
    # Generate stylized images
    content_a_style_b, content_b_style_a = get_stylized(a, b)
    
    # Preprocess images
    content_a_style_b = preprocess(content_a_style_b)
    content_b_style_a = preprocess(content_b_style_a)
    
    # Save images
    save_imgs(content_a_style_b, outpath_content_a_style_b)
    save_imgs(content_b_style_a, outpath_content_b_style_a)

# Defining behaviour when called from command line
if __name__=="__main__":
    # Initialize ArgumentParser class
    parser = argparse.ArgumentParser(description = "[SCRIPT DESCRIPTION] Generates two sets of stylized images from two corpora. It pairs images from the two corpora randomly, and generates two new stylized images per pair. One with content of image a and style of image b, and vice versa.")
    
    # Add inpath a argument
    parser.add_argument(
        "-i",
        "--inpatha", 
        type = str,
        default = os.path.join("data", "content_vangogh_style_vangogh", "*2.jpg"), # Default path to corpus, when none is specified
        required = False,
        help= "str - path to image corpus a")
    
    # Add inpath b argument
    parser.add_argument(
        "-I",
        "--inpathb",
        type = str,
        default = os.path.join("data", "content_monet_style_monet", "*2.jpg"), # Default path to corpus, when none is specified
        required = False,
        help= "str - path to image corpus b")
    
    # Add inpath b argument
    parser.add_argument(
        "-o",
        "--outpatha",
        type = str,
        default = os.path.join("data", "content_vangogh_style_monet"), # Default path to corpus, when none is specified
        required = False,
        help= "str - path to output path of the stylized images with content_a_style_b")
    
    # Add inpath b argument
    parser.add_argument(
        "-O",
        "--outpathb",
        type = str,
        default = os.path.join("data", "content_monet_style_vangogh"), # Default path to corpus, when none is specified
        required = False,
        help= "str - path to output path of the stylized images with content_b_style_a")
    
    # Taking all the arguments we added to the parser and input into "args"
    args = parser.parse_args()
    
    # Perform main function
    main(args.inpatha, args.inpathb, args.outpatha, args.outpathb)
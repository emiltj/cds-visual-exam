#!/usr/bin/env python
'''
###############################################################
--------------- Import of modules and libraries ---------------
###############################################################
'''
import os, glob, argparse, cv2
import pandas as pd
from shutil import copyfile

'''
###############################################################
--------------- Import of modules and libraries ---------------
###############################################################
'''
def get_target_inf(targetpath):
    """
    Function which retrieves information on the target image (normalized rgb histogram and name of target image).
    
    Targetpath: String that points to target image
    """
    # Getting the filename of the target image
    target_name = os.path.split(targetpath)[-1]
    
    # Load target image, calculate histogram and normalize
    target = cv2.imread(targetpath)
    target_hist = cv2.calcHist([target], [0, 1, 2], None, [8, 8, 8], [0, 255, 0, 255, 0, 255]) 
    target_hist_norm = cv2.normalize(target_hist, target_hist, 0, 255, cv2.NORM_MINMAX)
    
    # Return target name and target histogram
    return target_name, target_hist_norm

def get_dist(filepath, target_hist_norm, target_name, targetpath):
    """
    Function which calculates RGB-histogram distances using the chi-square method, between target image and the corpus.
    
    Filepath: String that points to images in corpus
    Target_hist_norm: Target histogram, normalized
    Target_name: Name of target image
    Targetpath: String that points to target image
    """
    # Info for user in terminal
    print(f"[INFO] Calculating distances from corpus \"{filepath}\" to \"{target_name}\" ...")
    
    # Empty lists for appending to
    file_names = []
    distances_to_target = []
    
    # Filepath to corpus
    files = glob.glob(filepath)
    
    # Excluding the target
    files.remove(targetpath)
    
    # For each of the non-target files, get filename and calculate distance to target
    for file in files:
        # Get filename and append to list
        file_names.append(os.path.split(file)[-1])

        # For each file, read image, get histogram, normalize and calculate distance using the chi-square method
        img = cv2.imread(file)
        img_hist = cv2.calcHist([img], [0, 1, 2], None, [8, 8, 8], [0, 255, 0, 255, 0, 255])
        img_hist_norm = cv2.normalize(img_hist, img_hist, 0, 255, cv2.NORM_MINMAX)
        dist = round(cv2.compareHist(target_hist_norm, img_hist_norm, cv2.HISTCMP_CHISQR), 2) #Rounded to 2 decimal places
        distances_to_target.append(dist)
    
    # Info for user in terminal
    print(f"[INFO] Distances between the 3D color histogram of \"{target_name}\" and the corpus \"{filepath}\" have been calculated using the chi-square method.")    
        
    # Return file names and distances to target
    return file_names, distances_to_target

def save_df(file_names, distances_to_target, target_name):
    """
    Function which saves a .csv file with distances from corpus to target image (as well as the filenames)
    
    file_names: Names of the files in the corpus to which distances were calculated
    distances_to_target: List of distances to target. Same index as "file_names"
    target_name: Name of target image
    """
    # Create a df with the information on distances
    df = pd.DataFrame(list(zip(file_names, distances_to_target)),
                columns = ["filename", "distance"])
    
    # If the folder does not already exist, create it
    if not os.path.exists("out"):
        os.makedirs("out")
    
    # Create outpath for df and save
    outpath = os.path.join("out", f"distances_to_{target_name[:-4]}.csv")
    df.to_csv(outpath, index = False)
    
    # Info for user in terminal
    print(f"[INFO] A new file with the distances has been created succesfully: \"{outpath}\"")
    
    # Return dataframe
    return outpath, df

'''
##################################################################################
############################# Defining main function #############################
##################################################################################
'''
def main(targetpath, filepath):
    """
    Main function of the script.
    
    Targetpath: Path to target image
    Filepath: Path to image corpus
    """
    # Get target info
    target_name, target_hist_norm = get_target_inf(targetpath)
    
    # Get distances to target from corpus (and corpus filenames)
    file_names, distances_to_target = get_dist(filepath, target_hist_norm, target_name, targetpath)
    
    # Save information as .csv
    outpath, df = save_df(file_names, distances_to_target, target_name)
    
    # Find the distance and the filename of the image with the shortest chisquare distance to target image
    closest_image = df.loc[df['distance'].idxmin()]
    
    # Copy target image and closest image to out (and print to terminal)
    copyfile(targetpath, os.path.join("out", "target_image.jpg"))
    copyfile(os.path.join("data", closest_image[0]), os.path.join("out", "closest_image.jpg"))
    print(f"[INFO] The target image (\"{target_name})\" and the closest image (\"{closest_image[0]})\" have been saved to \"out\". The chi-square histogram distance was found to be: {closest_image[1]}")
    
'''
###############################################################
----------- Defining use when called from terminal ------------
###############################################################
'''
if __name__=="__main__":
    # Initialize ArgumentParser class
    parser = argparse.ArgumentParser(description = "[SCRIPT DESCRIPTION] Calculates RGB-distance from image corpus to a specified target image using the chi-square method")
    
    # Add inpath argument
    parser.add_argument(
        "-f",
        "--filepath", 
        type = str,
        default = os.path.join("data", "*.jpg"), # Default path to corpus, when none is specified
        required = False,
        help= "str - path to image corpus")
    
    # Add outpath argument
    parser.add_argument(
        "-t",
        "--targetpath",
        type = str, 
        default = os.path.join("data", "image_0003.jpg"), # Default path to a target image, when none is specified
        required = False,
        help = "str - path to target file from which to calculate distance to the other images")
    
    # Taking all the arguments we added to the parser and input into "args"
    args = parser.parse_args()
    
    # Execute main function
    main(args.targetpath, args.filepath)

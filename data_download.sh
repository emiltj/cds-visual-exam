#! /bin/sh

# This script will download the required data from a google drive folder

# Install gdown
pip install gdown

# Install data

# Download data for assignment 2
cd assignment_2
mkdir data
cd data
printf "[INFO] Downloading data for assignment 2 ..."
gdown https://drive.google.com/uc?id=1A7Rlh76wJcQS5UbFgSbJLHy6ta-AiaHw # Download data
tar -xvzf flowers.tgz # Unzip
mv jpg/* . # Move all files down one folder
rm -r jpg files.txt flowers.tgz # Delete old folder and .tgz file
printf "\n\n[INFO] The required data for assignment 2 has been downloaded successfully"

# Download data for assignment 4
cd ../../assignment_4
mkdir data
cd data
printf "\n\n[INFO] Downloading data for assignment 4 ...\n\n"
gdown https://drive.google.com/uc?id=1LUNFekSNcIVNRjVkRSCFInb_FCMrqAr7 # Download data
printf "\n\n[INFO] The required data for assignment 4 has been downloaded successfully"

# Download data for assignment 5
cd ../../assignment_5
mkdir data
cd data
printf "\n\n[INFO] Downloading data for assignment 5 ...\n\n"
gdown https://drive.google.com/uc?id=1jqdfwGpUH4LOTAqkoTlqPJwCjg5wUwok # Download
unzip paintings.zip # Unzip
mv training/training/* training # Move images a level down
mv validation/validation/* validation # Move images a level down
rm -r paintings.zip training/training/ validation/validation/ # Remove old files, and unnecessary folders
printf "\n\n[INFO] The required data for assignment 5 has been downloaded successfully"

# Data for assignment_6 
cd ../..
mkdir -p assignment_6/data/content_cezanne_style_cezanne #Make new folders
mkdir assignment_6/data/content_monet_style_monet
cp assignment_5/data/training/Cezanne/* assignment_6/data/content_cezanne_style_cezanne/ # Copy training data of cezanne to new folder
cp assignment_5/data/validation/Cezanne/* assignment_6/data/content_cezanne_style_cezanne/ # Copy validation data of cezanne to new folder
cp assignment_5/data/training/Monet/* assignment_6/data/content_monet_style_monet/ # Copy training data of monet to new folder
cp assignment_5/data/validation/Monet/* assignment_6/data/content_monet_style_monet/ # Copy validation data of monet to new folder
rm assignment_6/data/content_monet_style_monet/9223372032559844173.jpg # Removing corrupt image file
printf "\n\n[INFO] The required data for assignment_6 has been downloaded successfully"

# Ending script
printf "\n\n[INFO] All required data has been downloaded"

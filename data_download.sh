#! /bin/sh

# This script will download the required data from a google drive folder

# Install gdown
pip install gdown

# Install data

# Download data for assignment 2
cd assignment_2
mkdir data
cd data
echo "[INFO] Downloading data for assignment 2 ..."
gdown ____
tar -xvzf data/flowers.tgz
mv flowers/* .
echo "[INFO] The required data for assignment 2 has been downloaded successfully"

# Download data for assignment 4
cd ../assignment_4
mkdir data
cd data
echo "[INFO] Downloading data for assignment 4 ..."
gdown ____
echo "[INFO] The required data for assignment 4 has been downloaded successfully"

# Download data for assignment 5
cd ../assignment_5
mkdir data
cd data
echo "[INFO] Downloading data for assignment 5 ..."
gdown ____
mv paintings/* .
echo "[INFO] The required data for assignment 5 has been downloaded successfully"

# Download data for self-assigned
cd ../self-assigned
mkdir data
echo "[INFO] Downloading data for self-assigned assignment ..."
for f in ___ ____ ____ ___ ; do gdown $f; done
echo "[INFO] The required data for the self-assigned assignment has been downloaded successfully"



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
gdown https://drive.google.com/uc?id=1A7Rlh76wJcQS5UbFgSbJLHy6ta-AiaHw
tar -xvzf flowers.tgz
mv jpg/* .
rm -r jpg files.txt flowers.tgz
printf "[INFO] The required data for assignment 2 has been downloaded successfully"

# Download data for assignment 4
cd ../../assignment_4
mkdir data
cd data
printf "\n\n[INFO] Downloading data for assignment 4 ...\n\n"
gdown https://drive.google.com/uc?id=1LUNFekSNcIVNRjVkRSCFInb_FCMrqAr7
echo "[INFO] The required data for assignment 4 has been downloaded successfully"

# Download data for assignment 5
cd ../../assignment_5
mkdir data
cd data
printf "\n\n[INFO] Downloading data for assignment 5 ...\n\n"
gdown https://drive.google.com/uc?id=1jqdfwGpUH4LOTAqkoTlqPJwCjg5wUwok
unzip paintings.zip
mv training/training/* training
mv validation/validation/* validation
rm -r paintings.zip training/training/ validation/validation/
printf "[INFO] The required data for assignment 5 has been downloaded successfully"

# Download data for self-assigned
#cd ../../self-assigned
#mkdir data
#cd data
#printf "\n\n[INFO] Downloading data for self-assigned assignment ...\n\n"
#for f in ___ ____ ____ ___ ; do gdown $f; done
#printf "[INFO] The required data for the self-assigned assignment has been downloaded successfully"

cd ../..

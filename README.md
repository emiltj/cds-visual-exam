
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/emiltj/cds-visual-exam">
    <img src="README_images/vis_logo.png" alt="Logo" width="200" height="200">
  </a>
  <h1 align="center">CDS Visual Analytics</h1>

  <p align="center">
    Exam portfolio
    <br />
    <a href="https://github.com/emiltj/cds-visual-exam/cds-visual-exam.pdf"><strong>Read about the project »</strong></a>
    <br />
    <a href="https://github.com/emiltj/cds-visual-exam/issues">Report Bug</a>
    ·
    <a href="https://github.com/emiltj/cds-visual-exam/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About the project</a></li>
    <li><a href="#getting-started">Getting started</a></li>
    <li><a href="#repository-structure">Repository structure</a></li>
    <li><a href="#assignments">Assignments</a></li>
    <li><a href="#data">Data</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About the project

<p align="center"><img src="README_images/analysis_example.png" alt="Logo" width="375" height="295"></p>
<p align="center"><em>Example image from one of the assignments</em>
</p>


This project contains the exam portofolio for the Spring 2021 module _Visual Analytics_ as part of the bachelor's tilvalg in [_Cultural Data Science_](https://bachelor.au.dk/en/supplementary-subject/culturaldatascience/) at Aarhus University. 
This README contains all the necessary information needed to get an overview of the repository, as well the installation steps required for running the scripts in the assignments. 

<!-- GETTING STARTED -->
## Getting started

For running my scripts I'd recommend following the below steps in your bash-terminal. This functions as a setup of the virtual environment, as well as an execution of a bash script that downloads all the data to the data folders respective to the assignments. 

### Cloning repository and creating virtual environment

The below code will clone the repository, as well as create a virtual environment

__MAC/LINUX/WORKER02__
```bash
git clone https://github.com/emiltj/cds-visual-exam.git
cd cds-visual
bash ./create_vis_venv.sh
```
__WINDOWS:__
```bash
git clone https://github.com/emiltj/cds-visual-exam.git
cd cds-visual
bash ./create_vis_venv_win.sh
```

### Retrieving the data

The data is not contained within this repository, considering the sheer size of the data. Using the provided bash script ```data_download.sh``` that I have created, the data will be downloaded from a Google Drive folder and automatically placed within the respective assignment directories. 

```bash
bash data_download.sh
```

After cloning the repo, creating the virutal environment and retrieving the data you should be ready to go. Move to the assignment folders and read the README's for further instructions.

<!-- REPOSITORY STRUCTURE -->
## Repository structure

This repository has the following structure:

| Column | Description|
|--------|:-----------|
```assignment_*/``` | Directory containing the four assignments
```utils/``` | Utility functions written by [Ross](https://pure.au.dk/portal/en/persons/ross-deans-kristensenmclachlan(29ad140e-0785-4e07-bdc1-8af12f15856c).html), utilized in a range of the assignments.
```README_images/``` | Directory containing the few images used in the README's.
```data_download.sh``` | Bash script that installs all the necessary data.
```create_vis_venv.*.sh``` | Bash scripts that automatically generates a new virtual environment, and install all the packages contained within ```requirements.txt```.
```kill_vision_venv.sh``` | Bash script that uninstalls and deletes the virtual environment.
```requirements.txt``` | A list of the required packages.
```.gitignore``` | A list of the files that git should ignore upon push/pulling (virtual environment and data).
```README.md``` | This very README file.

<!-- ASSIGNMENTS -->
## Assignments
Four assignments have been chosen for this portfolio and are included within the assignment directories. Information on script execution, preprocessing steps, results and discussion can be seen in the READMEs located within each of the assignment directories.

The four assignments are:
* Assignment 2 - Image search 
* Assignment 4 - Logistic Regression and Neural Network benchmark mnist classification
* Assignment 5 - CNN classification of impressionist paintings
* Assignment 6 - Stylized paintings and classification (self-assigned)

<!-- DATA -->
## Data
The datasets are provided by courtesy of:
- [Yann Lecun](http://yann.lecun.com/exdb/mnist/) - MNIST dataset
- [Maria-Elena Nilsback and Andrew Zisserman](https://www.robots.ox.ac.uk/~vgg/data/flowers/17/) - Flowers dataset
- [Panchajanya Banerjee](https://www.kaggle.com/delayedkarma/impressionist-classifier-data) - Impressionist paintings dataset

<!-- CONTACT -->
## Contact

Feel free to write me, Emil Jessen for any questions (also regarding the reviews). 
You can do so on [Slack](https://app.slack.com/client/T01908QBS9X/D01A1LFRDE0) or on [Facebook](https://www.facebook.com/emil.t.jessen/).

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Python](https://www.rstudio.com/) - Software used for conducting the analysis
* [othneildrew (githubuser)](https://github.com/othneildrew/Best-README-Template) - Providing a template used to create the README's
* [Ross Dean McLachlan](https://github.com/CDS-AU-DK/) - Our competent instructor for the module on Visual Analytics

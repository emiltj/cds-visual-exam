<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/emiltj/cds-visual-exam">
    <img src="../README_images/logo_au.png" alt="Logo" width="225" height="80">
  </a>
  
  <h3 align="center">Assignment 2</h3>

  <p align="center">
    Image search
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
    <li><a href="#assignment-description">Assignment description</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#methods">Methods</a></li>
    <li><a href="#results-and-discussion">Results and discussion</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ASSIGNMENT DESCRIPTION -->
## Assignment description

<!-- USAGE -->
## Usage

<!-- METHODS -->
## Methods

<!-- RESULTS AND DISCUSSION -->
## Results and discussion







# Assignment 5 - Visual Analytics

## Content of assignment

This folder contains the following:

| File | Description|
|--------|:-----------|
```cnn-artists.py```| Script that trains and validates a neural networks classifier on [impressionist paintings](https://www.kaggle.com/delayedkarma/impressionist-classifier-data). Can a machine-learning algorithm classify the artist of an impressionist painting? 
```out/```| A folder that contains the output of the script
```out/classification_report.csv```| The classification report
```out/model_plot.png```| A picture showing the model architecture
```out/training_history.png```| A plot showing the training history (accuracy and loss over epochs)


cnn-artists.py arguments:
- -- cnn (string - either "ShallowNet" or "LeNet")
- -- resizedim (tuple - a tuple containing resize parameters - the first two dimensions of the pictures are the resizing (height and width)
- -- batch_size (int - specifying batchsize)


## Running my scripts - MAC/LINUX/WORKER02
Setup
```bash
git clone https://github.com/emiltj/cds-visual.git
cd cds-visual
bash ./create_vis_venv.sh
```
Running this assignment:
```bash
cd cds-visual/assignment_5
source ../cv101/bin/activate 
python cnn-artists.py
```

## Running my scripts - WINDOWS
Setup
```bash
git clone https://github.com/emiltj/cds-visual.git
cd cds-visual
bash ./create_vis_venv_win.sh
```
Running this assignment:
```bash
cd cds-visual/assignment_5
source ../cv101/Scripts/activate 
python cnn-artists.py
``` 

## Contact

Feel free to write me, Emil Jessen for any questions (also regarding the reviews). 
You can do so on [Slack](https://app.slack.com/client/T01908QBS9X/D01A1LFRDE0) or on [Facebook](https://www.facebook.com/emil.t.jessen/).

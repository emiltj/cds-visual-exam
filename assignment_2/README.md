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











# Assignment 2 - Visual Analytics

## Content of assignment

This folder contains the following:

| File | Description|
|--------|:-----------|
```image_search.py```| Calculates distance from a target image, to a set of images within a folder

image_search.py arguments:
- --targetpath (str - path to target image.  Default = os.path.join("data", "image_0730.jpg"))
- --filepath (str - path to images from which to calculate distance to target image .csv file. Default = os.path.join("data", "*02.jpg"))

## Running my scripts - MAC/LINUX/WORKER02
Setup
```bash
git clone https://github.com/emiltj/cds-visual.git
cd cds-visual
bash ./create_vis_venv.sh
```
Running this assignment:
```bash
cd cds-visual/assignment_2
source ../cv101/bin/activate 
python image_search.py
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
cd cds-visual/assignment_2
source ../cv101/Scripts/activate 
python image_search.py
```

## Contact

Feel free to write me, Emil Jessen for any questions (also regarding the reviews). 
You can do so on [Slack](https://app.slack.com/client/T01908QBS9X/D01A1LFRDE0) or on [Facebook](https://www.facebook.com/emil.t.jessen/).

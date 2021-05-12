<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/emiltj/cds-visual-exam">
    <img src="../README_images/vis_logo.png" alt="Logo" width="200" height="200">
  </a>
  
  <h1 align="center">Assignment 2</h1>

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

This assignment compares rgb histograms of a target image and an image corpus. It utilizes the chi-square method to calculate the distances (rounded to two decimal places). Furthermore, the script saves a data frame with two column names; _filename_ and _distance_ - the name of the data frame is unique and identifies the chosen target image (e.g. _distances_to_<target_image_name>). Finally it prints the filename of the corpus image with the smallest distance to target.

The output can be found in ```assignment_2/out/```

<!-- USAGE -->
## Usage

Make sure to follow the instructions in the README.md located at the parent level of this repository, for the required installation of the virtual environment as well as the data download.
Subsequently, use the following code:

```bash
cd cds-visual/assignment_2
source ../cv101/bin/activate
python image_search.py
```

### Optional arguments:

image_search.py arguments for commandline to consider:
-       "-f"
        "--filepath", 
        type = str,
        default = os.path.join("data", "*.jpg"), # Default path to corpus, when none is specified
        required = False,
        help= "str - path to image corpus")
-       "-t"
        "--targetpath",
        type = str, 
        default = os.path.join("data", "image_0002.jpg"), # Default path to a target image, when none is specified
        required = False,
        help = "str - path to target file from which to calculate distance to the other images")

<!-- METHODS -->
## Methods


<!-- RESULTS AND DISCUSSION -->
## Results and discussion


<!-- CONTACT -->
## Contact

Feel free to write me, Emil Jessen for any questions.
You can do so on [Slack](https://app.slack.com/client/T01908QBS9X/D01A1LFRDE0) or on [Facebook](https://www.facebook.com/emil.t.jessen/).

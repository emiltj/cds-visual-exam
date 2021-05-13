<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/emiltj/cds-visual-exam">
    <img src="../README_images/vis_logo.png" alt="Logo" width="200" height="200">
  </a>
  <h1 align="center">Assignment 4</h1>
  
  <p align="center">
    Logistic Regression and Neural Network benchmark mnist classification
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




This assignment includes two scripts; one which utilizes linear regression and what which utilitizes neural networks.
The first script ```lr-mnist.py``` Trains a linear regression classifier on a subset of the MNIST dataset, with the possibility of setting parameters through terminal use. Subsequently it tests on another part of the MNIST dataset and outputs a classification report. Furthermore, the script has the feature of individual image prediction - making predictions of new images (even with different dimensions) possible. The second script ```nn-mnist.py``` has the same function, except it utilizes a neural network algorithm instead of linear regression.

Both scripts outputs classification reports in the terminal, but additionally also saves both classification report as well as the trained model to the folder ```assignment_4/out/```, when using the _save_ argument.

<!-- USAGE -->
## Usage

Make sure to follow the instructions in the README.md located at the parent level of this repository, for the required installation of the virtual environment as well as the data download.
Subsequently, use the following code:

```bash
cd cds-visual/assignment_2
source ../cv101/bin/activate
python lr_mnist.py
python nn_mnist.py
```

### Optional arguments:

lr_mnist.py arguments for commandline to consider:
-       "-o"
        "--outname",
        type = str,
        default = "classif_report_logistic_regression.csv", # Default when not specifying name of outputfile
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "str - containing name of classification report.")
-       "-s"
        "--save", 
        type = bool,
        default = True, # Default when not specifying anything else
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "bool - specifying whether to save classification report.")
-       "-i"
        "--individual", 
        type = str,
        default = os.path.join("data", "test.png"), # Default when not specifying anything in the terminal
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "str - specifying a .png file which is to be classified using this logistic regression model.")
-       "-p"
        "--penalty", 
        type = str,
        default = "none", # Default when not specifying anything in the terminal
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "str - specifying penalty for the classifier - possible values: \"none\", \"l1\", \"l2\", \"elasticnet\"")
-       "-c"
        "--c", 
        type = float,
        default = 1.0, # Default when not specifying anything in the terminal
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "int - specifying c-parameter for the classifier. recommended values: 0.01, 0.1, 1.0, 10, 100, where lower values mean stronger regularization")

nn_mnist.py arguments for commandline to consider:
-       "-o"
        "--outname", 
        type = str,
        default = "classif_report_neural_networks.csv", # Default when not specifying name of outputfile
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "str - containing name of classification report")
-       "-s"
        "--save", 
        type = bool,
        default = True, # Default when not specifying 
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "bool - specifying whether to save classification report")
-       "-i"
        "--individual", 
        type = str,
        default = os.path.join("data", "test.png"), # Default when not specifying anything in the terminal
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "str - specifying a .png file which is to be classified using this neural networks model.")
-       "-H"
        "--hiddenlayers", 
        type = list,
        default = [8, 16], # Default when not specifying anything in the terminal
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "list - specifying the hidden layers, each element in the list corresponds to number of nodes in layer. index in list corresponds to hiddenlayer number. E.g. [8, 16]")
-       "-e"
        "--epochs", 
        type = int,
        default = 50, # Default when not specifying anything in the terminal
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "int - specifying number of epochs for training the model. Default = 50")


<!-- METHODS -->
## Methods

<!-- RESULTS AND DISCUSSION -->
## Results and discussion

<!-- CONTACT -->
## Contact

Feel free to write me, Emil Jessen for any questions.
You can do so on [Slack](https://app.slack.com/client/T01908QBS9X/D01A1LFRDE0) or on [Facebook](https://www.facebook.com/emil.t.jessen/).

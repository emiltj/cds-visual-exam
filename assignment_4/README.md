<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/emiltj/cds-visual-exam">
    <img src="../README_images/vis_logo.png" alt="Logo" width="200" height="200">
  </a>
  <h1 align="center">Assignment 4</h1>
  
  <p align="center">
    Logistic Regression and Neural Network benchmark MNIST classification
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

Create two command-line tools which can be used to perform a simple classification task on the MNIST data and print the output to the terminal. These scripts can then be used to provide easy-to-understand benchmark scores for evaluating these models.
- Include two scripts; one with neural networks and one with logistic regression
- \[BONUS\] Both scripts output a classification report to the terminal and saves it as well
- \[BONUS\] Allow the user to determine number and size of layers for the Neural Network
- \[BONUS\] Allow the user to determine parameters for the Logistic Regression
- \[BONUS\] Allow the user to add an unseen data of any dimensions, process it, and let the classifier classify the new image
- \[BONUS\] Allow the user to save the neural network model for future use

This assignment includes two scripts; one which utilizes linear regression and what which utilitizes neural networks.
The first script ```lr-mnist.py``` Trains a linear regression classifier on a subset of the MNIST dataset, with the possibility of setting parameters through terminal use. Subsequently it tests on another part of the MNIST dataset and outputs a classification report. Furthermore, the script has the feature of individual image prediction - making predictions of new images (even with different dimensions) possible. The second script ```nn-mnist.py``` has the same function, except it utilizes a neural network algorithm instead of logistic regression.

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
**Specifically for this assignment:**

Prior to training, both scripts had the data min-max scaled to allow for faster processing and better convergence. Both the training and test data was scaled using the values of the training data, to avoid information to flow from the training set to the test set.
These scripts allows for simple model benchmarking on the MNIST dataset, which could prove useful if one wanted to test other models for classification of the same dataset.

Moreover, the \[BONUS\] features were included. This means that the user is allowed to specify parameters such as number of epochs, hiddenlayers for the Neural Network, while the arguments for the Logistic Regression script lets the user specify C-values and the penalty method. The classification reports can be saved if specified using the arguments, and the user can furthermore predict any new images (regardless of dimensions) using the argument _--individual__ 

**On a more general level (this applies to all assignments):**

I have tried to as accessible and user-friendly as possible. This has been attempted by the use of:
- Smaller functions. These are intended to solve the sub-tasks of the assignment. This is meant to improve readability of the script, as well as simplifying the use of the script.
- Information prints. Information is printed to the terminal to allow the user to know what is being processed in the background
- Argparsing. Arguments that let the user determine the behaviour and paths of the script (see "Optional arguments" section for more information)

<!-- RESULTS AND DISCUSSION -->
## Results and discussion

**Logistic regression classification report**
|           | 0                  | 1                 | 2                  | 3                  | 4                  | 5                  | 6                  | 7                  | 8                  | 9                  | accuracy | macro avg          | weighted avg       | 
|-----------|--------------------|-------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|----------|--------------------|--------------------| 
| precision | 0.9651741293532339 | 0.930327868852459 | 0.9123711340206185 | 0.8959276018099548 | 0.9132947976878613 | 0.8698224852071006 | 0.9606741573033708 | 0.9317073170731708 | 0.8918918918918919 | 0.9130434782608695 | 0.919    | 0.918423486146053  | 0.9186311211849802 | 
| recall    | 0.9797979797979798 | 0.978448275862069 | 0.9123711340206185 | 0.88               | 0.9575757575757575 | 0.8596491228070176 | 0.95               | 0.9408866995073891 | 0.8333333333333334 | 0.8974358974358975 | 0.919    | 0.9189498200340063 | 0.919              | 
| f1-score  | 0.9724310776942355 | 0.953781512605042 | 0.9123711340206185 | 0.8878923766816144 | 0.9349112426035504 | 0.8647058823529411 | 0.9553072625698323 | 0.9362745098039216 | 0.8616187989556137 | 0.9051724137931034 | 0.919    | 0.9184466211080473 | 0.9185747048733469 | 
| support   | 198.0              | 232.0             | 194.0              | 225.0              | 165.0              | 171.0              | 180.0              | 203.0              | 198.0              | 234.0              | 0.919    | 2000.0             | 2000.0             | 

**Neural networks classification report**
|           | 0                  | 1                  | 2                  | 3                  | 4                  | 5                  | 6                  | 7                  | 8                  | 9                  | accuracy | macro avg          | weighted avg       | 
|-----------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|----------|--------------------|--------------------| 
| precision | 0.9095238095238095 | 0.9696969696969697 | 0.9230769230769231 | 0.8528138528138528 | 0.8928571428571429 | 0.852760736196319  | 0.9130434782608695 | 0.8947368421052632 | 0.8563829787234043 | 0.8502024291497976 | 0.8915   | 0.8915095162404352 | 0.8918247844595311 | 
| recall    | 0.9646464646464646 | 0.9655172413793104 | 0.8041237113402062 | 0.8755555555555555 | 0.9090909090909091 | 0.8128654970760234 | 0.9333333333333333 | 0.9211822660098522 | 0.8131313131313131 | 0.8974358974358975 | 0.8915   | 0.8896882188998866 | 0.8915             | 
| f1-score  | 0.9362745098039216 | 0.9676025917926565 | 0.859504132231405  | 0.8640350877192982 | 0.9009009009009009 | 0.8323353293413173 | 0.9230769230769231 | 0.9077669902912622 | 0.8341968911917099 | 0.8731808731808732 | 0.8915   | 0.8898874229530268 | 0.8909608472780384 | 
| support   | 198.0              | 232.0              | 194.0              | 225.0              | 165.0              | 171.0              | 180.0              | 203.0              | 198.0              | 234.0              | 0.8915   | 2000.0             | 2000.0             | 


When looking at the results, the classification benchmarks for the Logistic Regression (LR) classifier and the Neural Networks (NN) classifier seem to have similar performance, with a macro average f1-score of .92 and * , respectively. NN's tend to outperform LR classifiers when both data and training time is plentiful and given the right hidden layer structure and parameter settings. The NN classifiers do, as here, however often take longer to train.
When looking at the performances for the individual numbers, it becomes evident that the classifer did not classify equally well for all numbers. 3, 5 and 8 seem to be harder to predict - this is likely due to the similarity that they may have with other numbers (i.e. pixels of 3 and 5 might have a lot of overlapping). 
As for out of sample images the scripts were also capable of classifying the individual test image of a written number, correctly classifying it as 4.

In conclusion, the classification reports serve as benchmarks that might be used when evaluating new models for classification purposes: _how well does another model compare in comparison to the relatively simple models used here?_

<!-- CONTACT -->
## Contact

Feel free to write me, Emil Jessen for any questions.
You can do so on [Slack](https://app.slack.com/client/T01908QBS9X/D01A1LFRDE0) or on [Facebook](https://www.facebook.com/emil.t.jessen/).

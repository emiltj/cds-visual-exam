<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/emiltj/cds-visual-exam">
    <img src="../README_images/vis_logo.png" alt="Logo" width="200" height="200">
  </a>
  <h2 align="center">Logistic Regression and Neural Network benchmarking</h2>
  
  <p align="center">
    Assignment 4
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
    <li><a href="#methods">Methods</a></li>
    <li><a href="#results-and-discussion">Results and discussion</a></li>
    <li><a href="#usage">Usage</a></li>
          <ul>
        <li><a href="#optional-arguments">Optional arguments</a></li>
      </ul>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ASSIGNMENT DESCRIPTION -->
## Assignment description

Create two command-line tools which can be used to perform a simple classification task on the MNIST data and print the output to the terminal. These scripts can then be used to provide easy-to-understand benchmark scores for evaluating these models.
* Include two scripts; one with neural networks and one with logistic regression
* \[BONUS\] Both scripts output a classification report to the terminal and saves it as well
* \[BONUS\] Allow the user to determine number and size of layers for the Neural Network
* \[BONUS\] Allow the user to determine parameters for the Logistic Regression
* \[BONUS\] Allow the user to add an unseen data of any dimensions, process it, and let the classifier classify the new image
* \[BONUS\] Allow the user to save the neural network model for future use

<!-- METHODS -->
## Methods
**Specifically for this assignment:**

Prior to training, both scripts had the data min-max scaled to allow for faster processing and better convergence. Both the training and test data was scaled using the values of the training data, to avoid information to flow from the training set to the test set.
These scripts allows for simple model benchmarking on the MNIST dataset, which could prove useful if one wanted to test other models for classification of the same dataset.

Moreover, all the "\[BONUS\]" features were included. This means that the user is allowed to specify parameters such as number of epochs and hiddenlayers for the Neural Network (NN), while the arguments for the Logistic Regression (LR) script lets the user specify C-values and penalty method. The classification reports can be saved if specified using the arguments, and the user can furthermore predict any new images (regardless of dimensions and colors) using the argument _--individual_.

**On a more general level (this applies to all assignments):**

I have tried to as accessible and user-friendly as possible. This has been attempted by the use of:
* Smaller functions. These are intended to solve the sub-tasks of the assignment. This is meant to improve readability of the script, as well as simplifying the use of the script.
* Information prints. Information is printed to the terminal to allow the user to know what is being processed in the background
* Argparsing. Arguments that let the user determine the behaviour and paths of the script (see <a href="#optional-arguments">"Optional arguments"</a> section for more information)

<!-- RESULTS AND DISCUSSION -->
## Results and discussion

#### Classification reports
|           | 0                  | 1                 | 2                  | 3                  | 4                  | 5                  | 6                  | 7                  | 8                  | 9                  | accuracy | macro avg          | weighted avg       | 
|-----------|--------------------|-------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|----------|--------------------|--------------------| 
| precision | 0.96 | 0.93 | 0.91 | 0.89 | 0.91 | 0.86 | 0.96 | 0.93 | 0.89 | 0.91 | 0.91    | 0.91  | 0.91 | 
| recall    | 0.97 | 0.97 | 0.91 | 0.88               | 0.95 | 0.85 | 0.95               | 0.94 | 0.83 | 0.89 | 0.91    | 0.91 | 0.919              | 
| f1-score  | 0.97 | 0.95 | 0.91 | 0.88 | 0.93 | 0.86 | 0.95 | 0.93 | 0.86 | 0.90 | 0.91    | 0.91 | 0.91 | 
| support   | 198.0              | 232.0             | 194.0              | 225.0              | 165.0              | 171.0              | 180.0              | 203.0              | 198.0              | 234.0              | 0.919    | 2000.0             | 2000.0             | 
<p align="center"><em>Logistic regression classification report</em></p>

<br/>

|           | 0                  | 1                  | 2                  | 3                  | 4                  | 5                  | 6                  | 7                  | 8                  | 9                  | accuracy | macro avg          | weighted avg       | 
|-----------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|----------|--------------------|--------------------| 
| precision | 0.94 | 0.96 | 0.91 | 0.91 | 0.88 | 0.90 | 0.94 | 0.91 | 0.89 | 0.90 | 0.92     | 0.91 | 0.91 | 
| recall    | 0.95 | 0.97 | 0.91 | 0.91 | 0.92 | 0.84  | 0.93 | 0.93 | 0.90 | 0.88 | 0.92     | 0.91 | 0.92               | 
| f1-score  | 0.95               | 0.96 | 0.91 | 0.91 | 0.90 | 0.87 | 0.94 | 0.92 | 0.89 | 0.89 | 0.91     | 0.91 | 0.91 | 
| support   | 198.0              | 232.0              | 194.0              | 225.0              | 165.0              | 171.0              | 180.0              | 203.0              | 198.0              | 234.0              | 0.92     | 2000.0             | 2000.0             | 
<p align="center"><em>Neural networks classification report</em></p>


When looking at the results, the classification benchmarks for the LR classifier and the NN classifier seem to have similar performance, with a macro average f1-scores of .91 for both models. NN's tend to outperform LR classifiers when both data and training time is plentiful and given the right hidden layer structure and parameter settings. As NN classifiers often take longer to train, the default parameters (hidden layer structure and number of epochs) were set to result in low runtimes for faster processing. More training would likely have resulted in higher performance.

When looking at the performances for the individual numbers, it becomes evident that the classifer did not classify equally well for all numbers. 3, 5 and 8 seem to be harder to predict - this is likely due to the similarity that they may have with other numbers (i.e. pixels of 3 and 5 might have a lot of overlapping). 
As for out of sample images the scripts were also capable of classifying the individual test image of a written number, correctly classifying it as 4.

In conclusion, the classification reports serve as benchmarks that might be used when evaluating new models for classification purposes: _how well does another model compare in comparison to the relatively simple models used here?_

<!-- USAGE -->
## Usage

Make sure to follow the instructions in the README.md located at the parent level of this repository, for the required installation of the virtual environment as well as the data download.

Subsequently, use the following code (when within the ```cds-visual-exam``` folder):

```bash
cd assignment_4
source ../cv101/bin/activate # If not already activated
python lr-mnist.py
python nn-mnist.py
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

<!-- CONTACT -->
## Contact

Feel free to write me, Emil Jessen for any questions.
You can do so on [Slack](https://app.slack.com/client/T01908QBS9X/D01A1LFRDE0) or on [Facebook](https://www.facebook.com/emil.t.jessen/).

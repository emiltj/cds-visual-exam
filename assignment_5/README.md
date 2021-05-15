<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/emiltj/cds-visual-exam">
    <img src="../README_images/vis_logo.png" alt="Logo" width="200" height="200">
  </a>
  <h1 align="center">Assignment 5</h1>

  <p align="center">
    CNN classification of impressionist paintings
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

Build and train a deep neural networks classifier to classify artists of [impressionist paintings](https://www.kaggle.com/delayedkarma/impressionist-classifier-data). Can a machine-learning algorithm classify the artist of an impressionist painting? Use either the architecture _ShallowNet_ or _LeNet_.
You should save visualizations showing loss/accuracy of the model during training; you should also a save the output from the classification report.


<!-- USAGE -->
## Usage

Make sure to follow the instructions in the README.md located at the parent level of this repository, for the required installation of the virtual environment as well as the data download.
Subsequently, use the following code:

```bash
cd cds-visual/assignment_2
source ../cv101/bin/activate
python cnn-artists.py
```

### Optional arguments:

cnn-artists.py arguments for commandline to consider:
-       "--cnn", 
        type = str,
        default = "ShallowNet",
        required = False,
        help = "str - specifying cnn architecture, use either \"ShallowNet\" or \"LeNet\"")
-       "--resizedim",
        type = list, 
        default = [32, 32],
        required = False,
        help = "list - specifying dimensions that the pictures should be resized to, e.g. [32, 32]")
-       "--batch_size",
        type = int, 
        default = 200,
        required = False,
        help = "int - specifying batch size")
-       "--epochs",
        type = int, 
        default = 50,
        required = False,
        help = "int - specifying number of epochs")

<!-- METHODS -->
## Methods

**Specifically for this assignment:**

Using a compact looped structure, the paintings of the individual artists were loaded into working memory. As the CNN we use requires data in the same format, the loaded paintings were resized and converted into the right format. To improve the versatility of the script, the user is given the option of choosing between either _LeNet_ or _ShallowNet_, as well as specifying resized dimensions of the images, batch size of the script, and also number of epochs for training. Classification reports are saved to the folder ```out/```, a long with a plot showing the architecture and a plot of the training history (the relationship between training epochs and the loss/accuracy of the model.

**On a more general level (this applies to all assignments):**

I have tried to as accessible and user-friendly as possible. This has been attempted by the use of:
- Smaller functions. These are intended to solve the sub-tasks of the assignment. This is meant to improve readability of the script, as well as simplifying the use of the script.
- Information prints. Information is printed to the terminal to allow the user to know what is being processed in the background
- Argparsing. Arguments that let the user determine the behaviour and paths of the script (see "Optional arguments" section for more information)


<!-- RESULTS AND DISCUSSION -->
## Results and discussion
**_ShallowNet_ architecture classification report**
|           | Cezanne             | Degas               | Gauguin             | Hassam             | Matisse             | Monet               | Pissarro            | Renoir              | Sargent             | VanGogh             | accuracy            | macro avg           | weighted avg        | 
|-----------|---------------------|---------------------|---------------------|--------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------| 
| precision | 0.2193877551020408  | 0.4411764705882353  | 0.42045454545454547 | 0.2345679012345679 | 0.45454545454545453 | 0.3287671232876712  | 0.3629032258064516  | 0.43137254901960786 | 0.49206349206349204 | 0.38461538461538464 | 0.34040404040404043 | 0.37698539017174515 | 0.37698539017174515 | 
| recall    | 0.43434343434343436 | 0.15151515151515152 | 0.37373737373737376 | 0.3838383838383838 | 0.20202020202020202 | 0.24242424242424243 | 0.45454545454545453 | 0.4444444444444444  | 0.31313131313131315 | 0.40404040404040403 | 0.34040404040404043 | 0.3404040404040404  | 0.34040404040404043 | 
| f1-score  | 0.29152542372881357 | 0.2255639097744361  | 0.39572192513368987 | 0.2911877394636015 | 0.2797202797202797  | 0.27906976744186046 | 0.40358744394618834 | 0.43781094527363185 | 0.38271604938271603 | 0.3940886699507389  | 0.34040404040404043 | 0.33809921538159565 | 0.33809921538159565 | 
| support   | 99.0                | 99.0                | 99.0                | 99.0               | 99.0                | 99.0                | 99.0                | 99.0                | 99.0                | 99.0                | 0.34040404040404043 | 990.0               | 990.0               | 

**_LeNet_ architecture classification report**
|           | Cezanne             | Degas               | Gauguin             | Hassam              | Matisse             | Monet               | Pissarro            | Renoir             | Sargent             | VanGogh             | accuracy           | macro avg           | weighted avg        | 
|-----------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|--------------------|---------------------|---------------------|--------------------|---------------------|---------------------| 
| precision | 0.2631578947368421  | 0.29213483146067415 | 0.39080459770114945 | 0.38636363636363635 | 0.32857142857142857 | 0.302158273381295   | 0.24193548387096775 | 0.34375            | 0.4186046511627907  | 0.3763440860215054  | 0.3191919191919192 | 0.33438248832702894 | 0.33438248832702894 | 
| recall    | 0.10101010101010101 | 0.26262626262626265 | 0.3434343434343434  | 0.1717171717171717  | 0.23232323232323232 | 0.42424242424242425 | 0.6060606060606061  | 0.3333333333333333 | 0.36363636363636365 | 0.35353535353535354 | 0.3191919191919192 | 0.3191919191919192  | 0.3191919191919192  | 
| f1-score  | 0.14598540145985403 | 0.2765957446808511  | 0.3655913978494624  | 0.23776223776223776 | 0.27218934911242604 | 0.35294117647058826 | 0.345821325648415   | 0.3384615384615385 | 0.3891891891891892  | 0.3645833333333333  | 0.3191919191919192 | 0.3089120693967896  | 0.3089120693967896  | 
| support   | 99.0                | 99.0                | 99.0                | 99.0                | 99.0                | 99.0                | 99.0                | 99.0               | 99.0                | 99.0                | 0.3191919191919192 | 990.0               | 990.0               | 

As can be seen in the tables (using default parameters), similar performance were found when utilizing the _LeNet_ and the _ShallowNet_ architecture, with slightly higher perfomance for the more complex architecture, _LeNet_. It achieved a macro average F1-score of _ , compared to the score of _ , that _ShallowNet_ achieved. When taking into account the fact that there are 10 artists and that each artist may paint various different portraits, these scores are relatively high.

Paintings from artists such as Monet seems to be easier to classify, compared to artists such as Cezanne. High performance for Monet, may very well be due to the fact that Monet's paintings almost always depicts the same subject matter - namely French landscapes. 

<p align="center"><a href="https://github.com/emiltj/cds-visual-exam/tree/main/assignment_2/out"><img src="./out/ShallowNet_training_history.png" alt="Logo" width="256" height="256">   <img src="./out/LeNet_training_history.png" alt="Logo" width="256" height="256"></a></p>

When looking at the training histories of the CNN following the _ShallowNet_ architecture ...

When looking at the training histories of the CNN following the _LeNet_ architecture



<!-- CONTACT -->
## Contact

Feel free to write me, Emil Jessen for any questions.
You can do so on [Slack](https://app.slack.com/client/T01908QBS9X/D01A1LFRDE0) or on [Facebook](https://www.facebook.com/emil.t.jessen/).
